#!/usr/bin/python
from PIL import Image
import os, sys

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
				
if len(sys.argv) == 2:
    len_cadena = len(sys.argv[1])
    cadena = sys.argv[1]
    caracter = cadena[len_cadena-1]
    if caracter == "/":
        path = sys.argv[1]
    else:
        path = sys.argv[1] + '/'
    dirs = os.listdir(path)
    resize()
else:
    print "Se debe pasar como argumento la ruta de los picons, ejemplo de llamada correcta: python resizepicon.py /media/hdd/picon"
