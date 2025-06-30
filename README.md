# TubeGrab

**TubeGrab** is a Flask-based web application that allows users to download YouTube videos and playlists in various formats. It is free, ad-free, privacy-friendly, and open source.

<!-- Optional badges -->
![License](https://img.shields.io/github/license/lappatdugain/Site-TubeGrab)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/platform-web--app-lightgrey)

---
## Features

- Download YouTube content as:
  - MP3 (audio only)
  - MP4 (video + audio)
  - MP4 HD (video only)
  - ZIP archives for full playlists
- Clean and responsive user interface
- No ads, no trackers, no user data collectio
- Safe downloads
- Open-source

## Installation

### Prerequisites

- Python 3.10 or newer
- `pip` for package management

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/lappatdugain/Site-TubeGrab.git
    cd Site-TubeGrab
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt 
    ```

3. Start the application:

    ```bash
    python app.py
    ```

---

---

## Usage

1. Launch your browser and navigate to:  
   `http://127.0.0.1:5000` (or your server’s domain/IP)

2. Select a tool:
   - **Video & Audio** – download a single video in multiple formats
   - **Playlist** – process and download entire playlists as ZIP

3. Paste the YouTube URL.

4. Choose your preferred format.

5. Click **Convert** or **Download**.

---
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

This project is licensed under the [GNU GPLv3](LICENSE).
## Contact

- Discord: [Join our Discord](https://discord.gg/qS2P3tqbp2)
- Email: [Contact Us](mailto:tubegrab.0bxdz@passinbox.com?subject=info%20TubeGrab)

##  Support
If you find this project helpful, consider supporting it:

- [Buy me a coffee](https://buymeacoffee.com/tubegrab)
