import logging
from datetime import datetime
import time
import os

import uuid

import tempfile
from zipfile import ZipFile, ZIP_DEFLATED
import shutil

from flask import Flask, render_template, flash, request, url_for, redirect, send_file, session, after_this_request

from pytubefix import YouTube, Playlist
import sys

from models import clear_up_title, download_steams, setup_logging, delete_old_files, is_valid_youtube_url

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
setup_logging()


@app.route('/')
def index():   
     return render_template('index.html')


@app.route('/donation')
def donation():   
     return render_template('views/donation.html')


@app.route('/terms')
def terms():
    return render_template('views/terms.html')


@app.route('/privacy')
def privacy():
    return render_template('views/privacy.html')

@app.route('/build')
def build():   
     return render_template('views/in_build.html')


@app.route('/video-audio', methods=['POST', 'GET'])
def video_audio_download():
    full_date = datetime.today().strftime("%Y-%m-%d %H:%M")
    
    if request.method == 'POST':
        url_form = request.form['url']
        conversion_type = request.form['conversion_type']
        logging.info(f"URL submitted: {url_form}")
        if is_valid_youtube_url(url_form):

            with tempfile.TemporaryDirectory() as tmp_file:
                if conversion_type in ["mp3", "mp4", "HD"]:               
                    try:
                        video = YouTube(url_form)
                        new_title=clear_up_title( video.title)
                        logging.info(f"Changing was effected on Original title : {video.title} New title : {new_title}")
                        
                        video_path=download_steams(url_form, conversion_type, full_date, new_title, tmp_file, video)

                        if video_path: 
                            unique_id = str(uuid.uuid4())
                            os.makedirs('/tmp/tubegrab', exist_ok=True)
                            filename = os.path.basename(video_path)
                            final_path = os.path.join('/tmp/tubegrab',filename)
                            session['download_path'] = final_path
                            shutil.move(video_path, final_path)
                     
                        else: 
                            logging.warning(f"Video {video.title} skipped — no path returned.")   
                            return render_template('views/video-audio.html', error_message_no_HD=f"{conversion_type} not available for this video")
                        
                        

                    except Exception as e:
                        logging.error(f"Error downloading video: {video.watch_url} — {e}")
                        return render_template('views/video-audio.html', error_message_no_HD="An error occurred during download.")
            
            return redirect(url_for('ready'))

        else: 
            return render_template('views/404.html')

    return render_template('views/video-audio.html')


@app.route('/playlist', methods=['POST', 'GET'])
def playlist_download():
    full_date = datetime.today().strftime("%Y-%m-%d %H:%M")
    
    if request.method == 'POST':
        url_form = request.form['url']
        conversion_type = request.form['conversion_type']
        logging.info(f"URL submitted: {url_form}")
        if is_valid_youtube_url(url_form):
        
            with tempfile.TemporaryDirectory() as tmp_file:
                if conversion_type in ["mp3", "mp4", "HD"]:
                    try:
                        playlist=Playlist(url_form)
                        new_playlist_title=clear_up_title(playlist.title)
                                                
                        zip_path = os.path.join(tmp_file, f"{new_playlist_title}.zip")
                        with ZipFile(zip_path, 'w', compression=ZIP_DEFLATED) as archive:
                            for video in playlist.videos:
                                try:
                                    new_title=clear_up_title( video.title)
                                    logging.info(f"Changing was effected on Original title : {video.title} New title : {new_title}")
                            
                                    video_path = download_steams(video.watch_url, conversion_type, full_date, new_title, tmp_file, video)
                                    
                                    if video_path:
                                        archive.write(video_path, arcname=os.path.basename(video_path))
                                    else:
                                        logging.warning(f"Video {video.title} skipped — no path returned.")   

                                except Exception as e:
                                    logging.error(f"Error downloading video: {video.watch_url} — {e}")
                        
                        unique_id = str(uuid.uuid4())
                        os.makedirs('/tmp/tubegrab', exist_ok=True)
                        final_path = os.path.join('/tmp/tubegrab', f'{unique_id}.zip')
                        session['download_path'] = final_path
                        shutil.move(zip_path, final_path)

                    except Exception as e:
                        logging.error(f"Playlist processing failed for URL: {url_form} — {e}")
                        return render_template('views/playlist.html', error_message_no_HD="An error occurred during playlist processing.")
            
            return redirect(url_for('ready'))

        else: 
            return render_template('views/404.html')

    return render_template('views/playlist.html')

@app.route('/ready')
def ready():
    if 'download_path' in session:
        return render_template('views/ready.html')
    return render_template('index.html'), 404


@app.route('/download')
def download():
    path = session.get('download_path')
    if not path or not os.path.exists(path):
        return render_template('views/404.html'), 404

    @after_this_request
    def cleanup(response):
        try:
            delete_old_files("/tmp/tubegrab/")
            os.remove(path)
            session.pop('download_path', None)
        except Exception as e:
            app.logger.error(f"Error deleting temp file: {e}")
        return response
        
    return send_file(path, as_attachment=True)





@app.errorhandler(404)
def page_not_found(error):
    return render_template('views/404.html'), 404
