'''
    Description: Download YouTube video's with python.
    Author: aulerjbailey
    Version: 1.0.0
    Video: https://youtu.be/gDiSwTOHcXk
'''
from pytube import YouTube

# Your url video of YouTube
url = ""

# Download
YouTube(url).streams.first().download()