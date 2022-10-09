import speech_recognition as sr
r = sr.Recognizer()

class audio2txt : 
    def audio2txt(rec,audiopath):
        with sr.AudioFile(audiopath) as source:
            audio = r.listen(source)
            try :
                text = r.recognize_google(audio)
                print ("Working on...")
                print(text)
                return text
            except:
                print("It is the bug from the audio2txt converter code....")



# og = audio2txt()
# txt = "male.wav"
# gt = og.audio2txt(txt)
