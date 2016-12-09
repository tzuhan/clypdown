#!/usr/bin/python
import clypdown
import os
import sys
import re
from subprocess import call

def downloadWithFile(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for url in lines:
            song_title, mp3_url = clypdown.get_mp3_url(url)
            print("song title")
            print(song_title)
            clypdown.download(mp3_url=mp3_url, title=song_title)

def convertOggToMp3():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.ogg')]
    for f in files:
        filename, ext = os.path.splitext(f)
        cmd = ["-i", '%s.ogg'%filename, "-vn", "-ar", "44100", "-ac", "2", "-ab", "192k", "-f", "mp3", '%s.mp3'%filename]
        call(["ffmpeg"] + cmd)


def main(args):
    #if len(args) != 2:
    #    sys.exit("Usage: python downloadwithfile.py filename")
    #downloadWithFile(args[1])
    convertOggToMp3()

if __name__ == "__main__":
    main(args=sys.argv)
