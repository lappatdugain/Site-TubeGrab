 # Changelog
All notable changes to this project will be documented in this file.

## [1.2.0] - 2025-08-01

### Added
- Introduced URL validation in video/playlist input forms to ensure correct YouTube URLs.
- Added proper accent handling in titles — accents are now preserved instead of being stripped.
- New template `ready.html` providing a waiting screen with a download button after processing.
- Added `/ready` and `/download` routes for managing download flow via temporary directories.
- Implemented cleanup mechanism to automatically delete temporary files older than 24 hours.

### Changed
- Improved UX by redirecting users to a "ready" state before download.
- Refined download logic to improve stability and reduce browser-related timeout risks.

### Upcoming
- [WIP] Celery integration in progress to offload long download tasks to background workers and avoid Apache 504 Gateway Timeout errors.
- Task ID management planned via cookies for async tracking.


## [1.1.1] - 2025-07-09

### Changed
- Replaced all static and route URLs in templates with `url_for()` for better Flask compatibility and flexibility.
- Updated view routing paths in `app.py`
- Improved CSS for better responsive behavior and cleaner `<main>` layout styling.
- Changed page titles for each template using Jinja block `{% block title %}` for clearer browser tab titles

### Added
- Created centralized logging module: `models/log.py`
  - Introduced `setup_logging()` function to streamline daily log file creation and standardize formatting across views.

### Fixed
- Adjusted internal form actions to use, ensuring compatibility if routes change.


## [1.1.0] - 2025-06-30

### Added
- New `donation.html` page displaying Bitcoin address and BuyMeACoffee QR code.
- Added `404.html` custom error page with message and return-to-home link.
- Introduced `in_build.html` placeholder view for future features.

### Changed
- Enhanced `playlist.html` functionality: now supports audio (MP3) and video (MP4) downloads for playlists.
- Removed donation sections from `video-audio.html` and `playlist.html` pages to keep the interface cleaner and less intrusive.
- Language support removed — all templates and content are now English-only for simplification and consistency.

### Removed
- `error.html` view removed. Errors are now logged exclusively in `LogsDownload-*.log` for better monitoring and cleaner UI.

### Fixed
- Improved playlist ZIP packaging to handle both audio and video content.
- Minor adjustments in navigation and footer for responsive layouts.

## [1.0.0] - 2025-06-26

### Added
- Complete application refactor following the CVM (Controller-View-Model) architecture pattern.
- Added playlist support with batch download as ZIP archive.
- New view `video-audio.html` for individual video/audio downloads.
- New view `playlist.html` for playlist processing and downloads.
- Introduced modular templating system with `base.html` layout and dedicated subviews.
- Reorganized static assets: separated into `images/` and `file-svg/` directories.
- Automatic daily logging in `app/Log/LogsDownload-*.log`.

### Changed
- Simplified `app.py` with better route separation (`/video-audio`, `/playlist`).
- Business logic extracted and moved into the `models/` directory.
- Improved title cleaning logic (removal of special characters and formatting issues).

### Fixed
- Fixed issues related to character encoding and malformed titles.
- Ensured proper closing of ZIP files after playlist processing.
- Improved error handling with clearer messages and fallback templates.

