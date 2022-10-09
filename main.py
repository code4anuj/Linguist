# import module
from pickle import FRAME
from click import option
from torch import true_divide
import streamlit as st
import sys
import subprocess
from pathlib import Path
import pip
from PIL import Image
import base64
import os
from importlib.resources import path
from fnmatch import translate
import cv2
from PIL import Image
from googletrans import Translator
import pytesseract

def tesseract():
    image = 'test.jpg'
    # pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image))
    print(text[:-1])
    txt = str(text[:-1])
    return txt


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://raw.githubusercontent.com/code4anuj/bgbgbg/main/newfinal3.jpg");
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

install('sentencepiece')
install('tenserflow')
# install('torch')
# install('transformers')
install('gtts')
install('playsound')
install('fpdf')
install('nltk')
install('networkx')
import networkx as nx
import nltk
from fpdf import FPDF
import gtts
# from gtts import gTTS
from playsound import playsound

from fnmatch import translate
import imp
from importlib.resources import path
from matplotlib.pyplot import text
from img2txt import img2txt
from pdf2text import pdf2txt
from translate import txt2translate
from audio2txt import audio2txt
from summerizer import generatesummary
import time

# attaching the translator model class
trnslt = txt2translate()

def img2translate(path,language):
    text = img.img2txt(path)
    translate = trnslt.txt2translate(text,language)
    print(translate)
    return translate

def pdf2translate(path,language):
    text = pdf.pdf2txt(path)
    translate = trnslt.txt2translate(text,language)
    print(translate)
    return translate

def audio2translate(path,language):
    text = audio.audio2txt(path)
    translate = trnslt.txt2translate(text,language)
    print(translate)
    return translate

# st.write(" Language Codes are as follow : hi=Hindi, bn=Bengali, ta=Tamil, te=Telugu, mr=Marathi, gu=Gujarati, ml=Malyalam")
lang_option = st.selectbox("Choose Target Language",
                     ['hindi','bengali','tamil','telugu','marathi','gujarati','malaylam'])

if (lang_option=="hindi"):
    lang_option = 'hi' 
elif (lang_option=="bengali"):
    lang_option ='bn'
elif (lang_option=="tamil"):
    lang_option ='ta'
elif (lang_option=="telugu"):
    lang_option ='te'
elif (lang_option=="marathi"):
    lang_option ='mr'
elif (lang_option=="gujarati"):
    lang_option ='gu'
elif (lang_option=="malaylam"):
    lang_option ='ml'


option = st.selectbox("Choose service",
                     ['Text Translate','Image Translate','Pdf Translate','Audio Translate','Summarize & Translate','RealTime Mode'])

# Text translator
if(option == "Text Translate"):
    # trnslt = txt2translate()
    text = st.text_input("Enter your TEXT here", "")
    if(st.button('Submit Text')):
        result = trnslt.txt2translate(text,lang_option)
        st.success(result)
       



# image translator

if(option == "Image Translate"):
    #importing the image path to the box 
    # imgpath = st.text_input("Enter the Path of the Image", "")
    imgpath = st.file_uploader("Upload Image ", type=['jpeg','jpg','png'])

    img = img2txt()
    # trnslt = txt2translate()
    if(st.button('Submit Image')):
        result = img2translate(imgpath,lang_option)
        st.write("Image Translated Succesfully...!! ")
        img = Image.open(imgpath)
        st.image(img, width=200)
        st.success(result)

# PDF translator

if(option == "Pdf Translate"):
    # pdfpath = st.text_input("Enter path of the PDF")
    file = st.file_uploader("Upload PDF File ", type='pdf')
    pdf = pdf2txt()
    # trnslt = txt2translate()
    if(st.button('Submit Pdf')):
        pdfpath = file.name
        result = pdf2translate(pdfpath,lang_option)
        st.write("PDF Translated Succesfully...!!")
        st.success(result)
        with open('pdftext.txt', 'w') as f:
            f.write(result)
        with open('pdftext.txt', "rb") as file:
            btn = st.download_button(
                    label="Download File",
                    data=file,
                    file_name="pdftext.txt",
                )

 


# Audio translator

if(option == "Audio Translate"):
    # audiopath = st.text_input("Enter path of Audio file")
    audiopath = st.file_uploader("Upload Audio File ", type=['wav','ogg'])
    audio = audio2txt()
    # trnslt = txt2translate()
    if(st.button('Submit Audio')):
        result = audio2translate(audiopath,lang_option)
        st.write("Audio Translated Succesfully...!!")
        st.success(result)
        sound=gtts.gTTS(result,lang="en",tld="co.in")
        sound.save("translatedaudio.wav")
        audio_file = open('translatedaudio.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        # playsound('translatedaudio.wav')
        with open("translatedaudio.wav", "rb") as file:
            btn = st.download_button(
                    label="Download audio",
                    data=file,
                    file_name="translatedaudio.wav",
                )
        
        

# Summarize & Translate
if(option == "Summarize & Translate"):
    # audiopath = st.text_input("Enter path of Audio file")
    file = st.file_uploader("Upload Text File ", type=['txt','docx'])

    summary = generatesummary()
    # trnslt = txt2translate()
    if(st.button('Submit File')):
        result_summary = summary.generatesummary(file.name)

        # providing one list 
        total=""
        for ele in range(0, len(result_summary)):
            total = total +str(result_summary[ele]) + "."
        
        st.success("Text Summarised Successfully...!! ")
        st.write(total)
        result_translate = trnslt.txt2translate(total,lang_option)
        st.write("Translation is loading ... ")
        st.success("Summary Translated Successfully...!! ")
        st.write("Translated Short Brief text is : ")
        st.write(result_translate)
        with open('summary.txt', 'w') as f:
            f.write(total)
        with open('summary.txt', "rb") as file:
            btn = st.download_button(
                    label="Download Summary",
                    data=file,
                    file_name="summary.txt",
                )
        with open('trasummary.txt', 'w') as f:
            f.write(result_translate)
        with open('trasummary.txt', "rb") as file:
            btn = st.download_button(
                    label="Download Translation Summary",
                    data=file,
                    file_name="trasummary.txt",
                )



# Real Time Mode
if(option=='RealTime Mode'):
    result = ""
    translator = Translator()
    run = st.checkbox('Run/Stop')
    FRAME_WINDOW = st.image([])
    cam = cv2.VideoCapture(0)
    while run:
        ret, frame = cam.read()
        
        cv2.imwrite('test.jpg',frame)
        en_text = tesseract()
        translator = Translator()
        txt = translator.translate(en_text, dest='hi')
        print(txt.text)
        result = str(txt.text)
        # st.success(txt.text)
        if result!="":
            st.success(result)
        FRAME_WINDOW.image(frame)
        if cv2.waitKey(1) & 0xff== 27:
            break
        
    else:
        cam.release()
        st.error("Camera Off !!")





