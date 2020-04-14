#This program is what the user runs, and is dependet on youtube-dl-simple.py
import time
from getpass import getpass
from youtube_dl_simple import youtubedl

print("-"*30)
print("If your source requires credentials, it needs to be inserted")
credentials = input("Do you wish to use credentials? (y/n): ")


if credentials.lower() == "y":
    credentials = True
    username = input("Please enter your username/mail: ")
    password = getpass()

elif credentials.lower() == "n":
    credentials = False

else:
    print("Invalid input")
    print("Assuming you want to run without credentials ;)")
    time.sleep(2)

url = input("Input the URL to the video or video library: ")

additional_args = input("Input additional argurments (blank for none): ")

if credentials == True:
    youtubedl(username, password, url)

elif credentials == False:
    youtubedl(url)
