import logging
from datetime import datetime
import time
import os

import tempfile
from zipfile import ZipFile, ZIP_DEFLATED

from flask import Flask, render_template, flash, request, url_for, redirect, send_file

from pytubefix import YouTube, Playlist
import sys

from models import clear_up_title, download_steams

app = Flask(__name__)


@app.route('/')
def index():   
     return render_template('index.html')

@app.route('/donation')
def donation():   
     return render_template('./views/donation.html')

@app.route('/video-audio', methods=['POST', 'GET'])
def video_audio_download():
    option_list=['mp3', 'mp4', 'HD']
    
    full_date = datetime.today().strftime("%Y-%m-%d %H:%M")
    date= datetime.today().strftime("%Y-%m-%d")

    logging.basicConfig(filename=f'../app/Log/LogsDownload-{date}.log',encoding="utf-8",level=logging.INFO)
    logging.getLogger('werkzeug').disabled = True
    
    if request.method == 'POST':

        url_form = request.form['url']
        conversion_type = request.form['conversion_type']
        logging.info(f"URL submitted: {url_form}")

        with tempfile.TemporaryDirectory() as tmp_file:
            if conversion_type in ["mp3", "mp4", "HD"]:               
                video = YouTube(url_form)
        
                new_title=clear_up_title( video.title)
                logging.info(f"Changing was effected on \n Original title : {video.title} \n New title : {new_title}")
                
                video_path=download_steams(url_form, conversion_type, full_date, new_title, tmp_file, video)

                if video_path is None: 
                    return render_template('./views/video-audio.html', error_message_no_HD=f"{conversion_type} not available for this video")
                else: 
                    return send_file(video_path, as_attachment=True)

    return render_template('./views/video-audio.html', error_message_no_HD='')


@app.route('/playlist', methods=['POST', 'GET'])
def playlist_download():
    full_date = datetime.today().strftime("%Y-%m-%d %H:%M")
    date= datetime.today().strftime("%Y-%m-%d")

    logging.basicConfig(filename=f'../app/Log/LogsDownload-{date}.log',encoding="utf-8",level=logging.INFO)
    logging.getLogger('werkzeug').disabled = True
    
    if request.method == 'POST':
        url_form = request.form['url']
        conversion_type = request.form['conversion_type']
        logging.info(f"URL submitted: {url_form}")
        
        with tempfile.TemporaryDirectory() as tmp_file:
            if conversion_type in ["mp3", "mp4", "HD"]:
                playlist=Playlist(url_form)
                new_playlist_title=clear_up_title(playlist.title)
                
                with ZipFile(os.path.join(tmp_file, f"{new_playlist_title}.zip"), 'w', compression=ZIP_DEFLATED) as archive:
                    
                    for video in playlist.videos:
                        new_title=clear_up_title( video.title)
                        logging.info(f"Changing was effected on \n Original title : {video.title} \n New title : {new_title}")
                    
                        video_path = download_steams(video.watch_url, conversion_type, full_date, new_title, tmp_file, video)
                        archive.write(video_path, arcname=os.path.basename(video_path))
            
            return send_file(archive.filename, as_attachment=True)

    return render_template('./views/playlist.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('./views/404.html'), 404

@app.route('/build')
def build():   
     return render_template('./views/in_build.html')