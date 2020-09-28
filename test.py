import os
import youtube_dl

url_list = ['https://www.youtube.com/watch?v=Sw2J4plpoYU']

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(os.getcwd(), 'music/%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
}

# On Windows get ffmpeg from folder
if os.name == 'nt':
    ydl_opts['ffmpeg_location'] = os.path.join(os.getcwd(), 'bin/codecs')

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url_list)
