#!/usr/bin/python
from PIL import Image
import os, sys
import shutil

path = sys.argv[1]
dirs = os.listdir(path)

def splitfilename(filename):
    sname = ""
    sext = ""
    i = filename.rfind(".")
    if (i != 0):
        n = len(filename)
        j = n-i-1
        sname = filename[0:i]
        sext = filename[-j:]    
    return sname, sext

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            sfilename, sext = splitfilename(item)
            if (sext == "png"):
                im = Image.open(path+item)
                f, e = os.path.splitext(path+item)
                imResize = im.resize((220,132), Image.ANTIALIAS)
                imResize.save(f+'.png', 'png')

resize()
