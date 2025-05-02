
# TubeGrabe

TubeGrabe is a Flask-based web application that allows users to download YouTube videos as MP3 or MP4 files. The service is free, without advertising, and respects user privacy by not collecting any data.

## Features

- Download YouTube videos in 
    - audio(mp3) 
    - video and autio (mp4)
    -HD video without audio(mp4)
- User-friendly interface.
- Free to use with no advertisements.
- No data collection or commercial cookies.
- Safe downloads.
- Open-source application

## Installation

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/lappatdugain/https://github.com/lappatdugain/Site-TubeGrab.git
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
2. Enter the URL of the YouTube video you want to download.
3. Choose the desired format (MP3 or MP4).
4. Click on the "Convert" button to start the download.

## Project Structure

## `TubeGrab/app.py`

The main entry point of the Flask application. It runs the server and defines the routes.
Contains the Flask views and logic for handling URL submissions and file conversions.

## `templates/index.html`

The HTML template for the main page. It includes:

- A form to submit the YouTube URL and select the conversion type (MP3 or MP4).
- Information about the service in both English and French.
- Navigation menu with links to home, donation page, and Discord.

## `templates/error.html`

The HTML template for the error page. 

## `static/`

Contains static files such as CSS, JavaScript, images, and SVG icons used in the web application.

## Logging

The application logs important events and errors to a file named `LogsDownload.log`.

## License

This project is open source and available under the [GPL-3.0 license](LICENSE).

## Contact

- Discord: [Join our Discord](https://discord.gg/qS2P3tqbp2)
- Email: [Contact Us](mailto:tubegrab.0bxdz@passinbox.com?subject=info%20TubeGrab)

## Donation

If you find this service useful, consider making a donation:

- [Buy me a coffee](https://buymeacoffee.com/tubegrab)
