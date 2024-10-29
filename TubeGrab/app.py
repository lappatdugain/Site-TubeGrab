import logging
from datetime import datetime
import time

import tempfile
import zipfile

from flask import Flask, render_template, flash, request, url_for, redirect, send_file

from pytubefix import YouTube, Playlist
from moviepy.editor import *

app = Flask(__name__)

# client={   1: "WEB", 2: "WEB_EMBED", 3: "WEB_MUSIC", 4: "WEB_CREATOR", 5: "WEB_SAFARI", 6: "ANDROID", 7: "ANDROID_MUSIC", 8: "ANDROID_CREATOR", 9: "ANDROID_VR", 10: "ANDROID_PRODUCER",
#     11: "ANDROID_TESTSUITE", 12: "IOS", 13: "IOS_MUSIC", 14: "IOS_CREATOR", 15: "MWEB", 16: "TV_EMBED", 17: "MEDIA_CONNECT"}

# Initialize logging

@app.route("/", methods=['POST', 'GET'])
def url():
    full_date = datetime.today().strftime("%Y-%m-%d %H:%M")
    date= datetime.today().strftime("%Y-%m-%d")
    logging.basicConfig(filename=f'./TubeGrab/Log/LogsDownload-{date}.log', level=logging.INFO)

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
                    print("video : ",url_form)
                    title_video = video.title
                    video.register_on_progress_callback(progression)
            
                    # Handle special characters in the video title
                    caractere_speciaux = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '&', '=', '?', '%', '『』', '「」']
                    for caractereSpecial in caractere_speciaux:
                        edit_title = title_video.replace(caractereSpecial, '_')
                    logging.info(f"Changing was effected on \n Original title : {video.title} \n New title : {edit_title}")

                    if conversion_type == 'mp3':
                        logging.info(f"Download completed for URL: {url_form} made on : {full_date} types : audio (mp3)")
                        audio_steams = video.streams.get_audio_only()
                        audio_steams.download(output_path=tmp_file, filename=f'{edit_title}.mp4')
                        audio_path = os.path.join(tmp_file, f'{edit_title}.mp3')

                        # Convert MP4 to MP3
                        with AudioFileClip(os.path.join(tmp_file, f'{edit_title}.mp4')) as audio:
                            audio.write_audiofile(audio_path)
                        """progression(flux)"""
                        
                        logging.info(f"MP3 download complete: {audio_path}")

                        # Send the MP3 file to the user
                        return send_file(audio_path, as_attachment=True)



                    if conversion_type == 'mp4':
                        logging.info(f"Download completed for URL: {url_form} made on : {full_date} types : video (mp4)")
                        video_steams = video.streams.get_highest_resolution()
                        video_steams.download(output_path=tmp_file, filename=f'{edit_title}.mp4')
                        video_path = os.path.join(tmp_file, f'{edit_title}.mp4')

                        logging.info(f"MP4 download complete: {video_path}")

                        # Send the MP4 file to the user
                        return send_file(video_path, as_attachment=True)

                    if conversion_type == 'HD':
                        logging.info(f"Download completed for URL: {url_form} made on : {full_date} types : video (HD)")
                        HD_video_steams=video.streams.filter(res="1080p",mime_type="video/mp4")
                        if not HD_video_steams:
                            return render_template("index.html", error_message_no_HD="HD not available for this video")
                        HD_video_steams.first().download(output_path=tmp_file, filename=f'{edit_title}.mp4')
                        HD_video_path = os.path.join(tmp_file, f'{edit_title}.mp4')

                        logging.info(f"MP4(HD) download complete: {HD_video_path}")

                        # Send the MP4 file to the user
                        return send_file(HD_video_path, as_attachment=True)

        return render_template("index.html")

    except Exception as e:
        print(e)
        return render_template("error.html",error_message =e)




if __name__ == "__main__":
    app.run(debug=True,port=5500)
