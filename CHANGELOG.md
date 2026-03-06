# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-03-06

### Added
- Integrated **Vite** as the modern bundler inside the `jslib/` directory, replacing the legacy `build.sh` and `jsmin` script workflow.
- Introduced a full, custom CSS glassmorphic design system inside `htdocs/public/css/main.css`.
- Added Day.js localization format (`localizedFormat` plugin) to keep legacy Moment.js formatting behavior (`L LTSZ`).
- Integrated **Redis** into the default Docker topology (`docker-compose.yml` and `docker-compose-rel.yml`) to memoize the heaviest PostgreSQL map sector aggregation operations on the WebSocket Server, radically enhancing performance.

### Changed
- Replaced the deprecated `Moment.js` dependency across the frontend application with `Day.js`, noticeably improving bundle sizes and rendering speed.
- Upgraded the `jQuery` dependency to version `3.7.1`.
- Upgraded `Font Awesome` to version `6.4.0` in the main templates.
- Polished structural HTML and syntax within modals (`#td-modal`, `#modal-timetravel`) and dynamic overlays (`#right-container`, `#bottominfo-container`) for a completely modern aesthetic.
- Replaced plaintext overlay navigation items with aesthetic FontAwesome icons inside top navbar dropdowns.

### Removed
- Removed the deprecated `build.sh` and `compile.php` legacy build pipeline scripts from `jslib/`.
