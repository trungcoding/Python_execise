from gtts import gTTS
import os
import csv
with open("/home/ngoctrung/directory_env/PythonWS/text.txt", "r") as file:
            my_text = file.read()
language = 'vi'
my_voice = gTTS(text= my_text, lang= language, slow= False)
my_voice.save('voiceFromText.mp3')