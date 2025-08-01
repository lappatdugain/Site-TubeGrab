"""
media_processor: A Python package for processing YouTube media,
including format selection, stream downloading, and title cleaning.

Includes:
- Video type validation (HD, MP4, MP3)
- Stream downloading and audio extraction
- Video title cleaning for safe filenames
"""

__title__ = "media_processor"
__author__ = "L'appatdugain"

# Media format logic & download
from models.utils import is_HD, is_mp3, is_mp4
from models.steams_formatter import download_steams

# Title cleaner
from models.clear_title import clear_up_title

# Logging setup
from models.log_config import setup_logging

# Temporary directory cleaner
from models.tmp_cleanup import delete_old_files


#Check url format
from models.url_formatter import is_valid_youtube_url