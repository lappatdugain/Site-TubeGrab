import os 
import time
from datetime import datetime
import logging
from moviepy import *
from flask import Flask, render_template, flash, request, url_for, redirect, send_file

from models import is_HD, is_mp4, is_mp3
from models.log_config import setup_logging

video_type_func = {'mp3': is_mp3, 'mp4': is_mp4, 'HD': is_HD}


def download_steams(url, video_type, date, title, tmp_path, video):
    
    setup_logging()
    
    result=video_steams=video_type_func[video_type](url, video_type, date, title, tmp_path, video)
    if result:
        result.download(output_path=tmp_path, filename=f'{title}.mp4')
        if video_type=='mp3':
            audio_steams = os.path.join(tmp_path, f'{title}.mp3')
            with AudioFileClip(os.path.join(tmp_path, f'{title}.mp4')) as audio:
                audio.write_audiofile(audio_steams)
            logging.info(f"MP3 download complete: {audio_steams}")
            return audio_steams
        else:
            video_steams = os.path.join(tmp_path, f'{title}.mp4')  
            logging.info(f"{video_type}) download complete: {video_steams}")
            return video_steams
    else : return None