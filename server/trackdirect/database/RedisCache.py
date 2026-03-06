import logging
import redis
import pickle
from server.trackdirect.TrackDirectConfig import TrackDirectConfig

class RedisCache:
    """The RedisCache class handles basic caching via Redis."""

    def __init__(self):
        """Initialize the RedisCache with configuration parameters."""
        config = TrackDirectConfig()
        self.logger = logging.getLogger('trackdirect')
        self.enabled = config.redis_enabled
        self.redis_client = None

        if self.enabled:
            try:
                self.redis_client = redis.Redis(
                    host=config.redis_host,
                    port=config.redis_port,
                    socket_connect_timeout=2
                )
                self.redis_client.ping()
                self.logger.info(f"Connected to Redis cache at {config.redis_host}:{config.redis_port}")
            except Exception as e:
                self.logger.warning(f"Failed to connect to Redis cache: {e}")
                self.enabled = False
                self.redis_client = None

    def get(self, key):
        """Retrieve a value from the cache.

        Args:
            key (str): The cache key.

        Returns:
            The unpickled value, or None if not found or disabled.
        """
        if not self.enabled or not self.redis_client:
            return None
        
        try:
            val = self.redis_client.get(key)
            if val is not None:
                return pickle.loads(val)
        except Exception as e:
            self.logger.warning(f"Redis get error for {key}: {e}")
            
        return None

    def set(self, key, value, ttl_seconds=60):
        """Store a value in the cache.

        Args:
            key (str): The cache key.
            value: The value to pickle and store.
            ttl_seconds (int): Time to live in seconds.
        """
        if not self.enabled or not self.redis_client:
            return

        try:
            self.redis_client.setex(key, ttl_seconds, pickle.dumps(value))
        except Exception as e:
            self.logger.warning(f"Redis set error for {key}: {e}")
