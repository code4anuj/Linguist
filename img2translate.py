from fnmatch import translate
import imp
from importlib.resources import path

from matplotlib.pyplot import text
from img2txt import img2txt
from translate import txt2translate

# image to txt 
img = img2txt()
imgpath = "img.png"
trnslt = txt2translate()

def img2translate(path,language):
    text = img.img2txt(path)
    translate = trnslt.txt2translate(text,language)
    print(translate)

img2translate(imgpath,language)
