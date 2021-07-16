import os
import random

from pygame.mixer import music
from pygame import mixer
from pygame import error as pygameError

mixer.init()

debug = True
file = ""
userpath = os.path.expanduser("~")
playedFiles = []

formats = ["wav","mp3","ogg"]

def playFile(file):
    try:
        if debug:
            print("playing now ->", file)
        playedFiles.append(file)
        music.load(file)
        music.play()
        while(music.get_busy()):
            pass
        music.unload()
    except pygameError:
        if debug:
            print(file, "is corrupted or unsupported by pygame")

def randomFile(Dir):
    global file

    try:
        fileName = random.choice(os.listdir(Dir))
        if ( os.path.isdir(Dir + os.path.sep + fileName) ):
            randomFile(Dir + os.path.sep + fileName)
        else:
            gotFormat = fileName.split(".")[-1]
            if gotFormat in formats and not((Dir + os.path.sep + fileName) in playedFiles):
                file = (Dir + os.path.sep + fileName)
                playedFiles.append(file)
    except (IndexError, PermissionError) as exception:
        randomFile(userpath)

while True:
    file = ""
    while file == "":
        randomFile(userpath)
    playFile(file)
