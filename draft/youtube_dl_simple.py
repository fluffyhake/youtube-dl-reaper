#This program contains the 
import os
import youtube_dl
import pprint



def download(url, **add_args):
    ydl_opts = {
}
    for key,value in add_args.items():
        ydl_opts[key] = value
        print(ydl_opts)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


#download(url = "https://www.youtube.com/watch?v=0Kvw2BPKjz0", format = "mp4")