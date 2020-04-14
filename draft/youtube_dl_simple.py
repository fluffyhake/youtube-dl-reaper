#This program contains the 
import os
import youtube_dl




ydl_opts = {

}

def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

