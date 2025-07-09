from datetime import datetime
import time
import logging
import os
from models.log_config import setup_logging

def is_mp3(url, video_type, date, title, tmp_path, video):
    log_file=setup_logging()
    MP3_video_steams=video.streams.get_audio_only()
    if MP3_video_steams is None:
        logging.warning(f"{video_type} not available for this video")
    else: 
        logging.info(f"Download completed for URL: {url} made on : {date} types : video ({video_type})")
        return MP3_video_steams

def is_mp4(url, video_type, date, title, tmp_path, video):
    date= datetime.today().strftime("%Y-%m-%d")
    log_dir = os.path.join(os.path.dirname(__file__), 'Log')
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f'LogsDownload-{date}.log')
    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.INFO)
    logging.getLogger('werkzeug').disabled = True
    MP4_video_steams=video.streams.get_highest_resolution()
    if MP4_video_steams is None:
        logging.warning(f"{video_type} not available for this video")
    else: 
        logging.info(f"Download completed for URL: {url} made on : {date} types : video ({video_type})")
        return MP4_video_steams

def is_HD(url, video_type, date, title, tmp_path, video):
    date= datetime.today().strftime("%Y-%m-%d")
    log_dir = os.path.join(os.path.dirname(__file__), 'Log')
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f'LogsDownload-{date}.log')
    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.INFO)
    logging.getLogger('werkzeug').disabled = True
    HD_video_steams=video.streams.filter(res="1080p",mime_type="video/mp4").first()
    if HD_video_steams is None:
        logging.warning(f"{video_type} not available for this video")
    else: 
        logging.info(f"Download completed for URL: {url} made on : {date} types : video ({video_type})")
        return HD_video_steams
