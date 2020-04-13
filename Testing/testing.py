from __future__ import unicode_literals
import youtube_dl
import time



print('-'*30)
print('The  Y O U T U B E - D L  suite')
print('-'*30)
time.sleep(2)

print("The URL can be to a specific video, to a channel, or to a playlist. The downloader wil rip it all!")
print('-'*30)
url = input("Please insert the desired video: ")

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
