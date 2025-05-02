"""
media_formatter: A module for selecting and downloading YouTube media streams (MP4, MP3, HD)
with format-specific logic and audio extraction support.

Includes:
- video type validation (HD, MP4, MP3)
- stream downloading and audio extraction
"""

__title__ = "media_formatter"
__author__ = "L'appatdugain"

from media_formatter.utils import is_HD, is_mp3, is_mp4
from media_formatter.steams_formatter import download_steams