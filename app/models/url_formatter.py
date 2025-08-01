import re 

url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def is_valid_youtube_url(url: str) -> bool:
    """
    Check if a URL is a valid YouTube or compatible frontend video/playlist URL.
    """

    youtube_patterns = [
        # Standard watch URLs
        r'^https?://(www\.)?youtube\.com/watch\?v=[\w\-]{11}(&.+)?$',
        # Shortened youtu.be links
        r'^https?://youtu\.be/[\w\-]{11}(\?.+)?$',
        # Shorts
        r'^https?://(www\.)?youtube\.com/shorts/[\w\-]{11}$',
        # Embed/nocookie
        r'^https?://(www\.)?youtube\-nocookie\.com/embed/[\w\-]{11}$',
        # Playlist URLs
        r'^https?://(www\.)?youtube\.com/playlist\?list=[\w\-]+$',
        r'^https?://(www\.)?youtube\.com/watch\?.*list=[\w\-]+(&.*)?$',
    ]

    for pattern in youtube_patterns:
        if re.match(pattern, url.strip()):
            return True
        