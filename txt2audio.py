from gtts import gTTS
import playsound
text= "Hello there "
sound=gtts.gTTS(text,lang="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")