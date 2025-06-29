 # Changelog
All notable changes to this project will be documented in this file.



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

