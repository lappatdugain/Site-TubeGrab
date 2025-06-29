
# TubeGrabe

**TubeGrab** is a Flask-based web application that allows users to download YouTube videos in various formats. It is free, ad-free, privacy-friendly, and open source.

## Features

- Download YouTube content in:
  - MP3 (audio only)
  - MP4 (video + audio)
  - MP4 HD (video only)
  - Full playlist downloads in a single ZIP archive
- Clean and responsive user interface
- No advertisements or tracking
- No data collection or commercial cookies
- Safe downloads
- Open-source and community-supported

## Installation

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/lappatdugain/Site-TubeGrab.git
    cd Site-TubeGrab
    ```

2. Install dependencies :
    ```bash
    pip install -r requirements.txt 
    ```

3. Run the application:

    ```bash
    python app.py
    ```

## Usage

1. Open your web browser and go to `www.[currently undefined]`.
2. Choose a tool:
    - Video & Audio: for individual video downloads
    - Playlist: for playlist download and ZIP export
3. Paste the YouTube URL.
4. Select your preferred format.
5. Click Convert or Download
## Project Structure

```
Site-TubeGrab/
│
├── app.py                       # Main application entry (Flask)
├── models/                      # Business logic (downloaders, validators, etc.)
├── templates/
│   ├── base.html                # Base layout
│   ├── video-audio.html         # Individual video/audio download page
│   ├── playlist.html            # Playlist ZIP download page
│   └── error.html               # Error handling page
│
├── static/
│   ├── css/                      # Stylesheets
│   ├── images/                   # Image assets
│   └── file-svg/                 # SVG icons
│
└── app/Log/                      # Download logs (e.g. LogsDownload-2025-06-26.log)
```
## Logging
The app automatically logs daily download activity and errors in files named like:
```
app/Log/LogsDownload-YYYY-MM-DD.log
```
## License

This project is open source and available under the [GPL-3.0 license](LICENSE).

## Contact

- Discord: [Join our Discord](https://discord.gg/qS2P3tqbp2)
- Email: [Contact Us](mailto:tubegrab.0bxdz@passinbox.com?subject=info%20TubeGrab)

## Donation

If you find this service useful, consider making a donation:

- [Buy me a coffee](https://buymeacoffee.com/tubegrab)
