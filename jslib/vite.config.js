import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    outDir: '../htdocs/public/js',
    emptyOutDir: false, // We only want to overwrite trackdirect.min.js, not empty the whole folder
    lib: {
      entry: resolve(__dirname, 'src/trackdirect.js'),
      name: 'trackdirect',
      fileName: () => 'trackdirect.min.js',
      formats: ['iife'], // Compile to an Immediately Invoked Function Expression for browser compatibility
    },
    minify: 'esbuild',
  },
});
