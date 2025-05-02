import logging
from datetime import datetime
import time
import os

import tempfile
import zipfile

from flask import Flask, render_template, flash, request, url_for, redirect, send_file

from pytubefix import YouTube, Playlist
import sys

from title_cleaner import clear_up_title
from media_formatter import download_steams

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def url():
    full_date = datetime.today().strftime("%Y-%m-%d %H:%M")
    date= datetime.today().strftime("%Y-%m-%d")
    logging.basicConfig(filename=f'./app/Log/LogsDownload-{date}.log',encoding="utf-8",level=logging.INFO)
    logging.getLogger('werkzeug').disabled = True

    
    option_list=['mp3', 'mp4', 'HD']
    
    functions = {"Download": download_steams,}



    def progression(stream, chunk, bytes_remaining):
        bytes_downloaded = stream.filesize - bytes_remaining
        percent = bytes_downloaded * 100 / stream.filesize
        print(f"Download progress: {int(percent)}%")

    try:
        if request.method == 'POST':
            url_form = request.form['url']
            conversion_type = request.form['conversion_type']
            logging.info(f"URL submitted: {url_form}")

            with tempfile.TemporaryDirectory() as tmp_file:
                if conversion_type in ["mp3", "mp4", "HD"]:               
                    video = YouTube(url_form)
            
                    title_video = video.title
                    video.register_on_progress_callback(progression)
            
                    new_title=clear_up_title(title_video)
                    logging.info(f"Changing was effected on \n Original title : {video.title} \n New title : {new_title}")
                    
                    final_resutl=video_path=functions["Download"](url_form, conversion_type, full_date, new_title, tmp_file, video)
                    if final_resutl is None: return render_template("index.html", error_message_no_HD=f"{conversion_type} not available for this video")
                    else: return send_file(video_path, as_attachment=True)

        return render_template("index.html", error_message_no_HD='')

    except Exception as e:
        return render_template("error.html",error_message =e)


# https://youtu.be/kLZJw_JAaMk

if __name__ == "__main__":
    app.run(debug=True,port=8888)