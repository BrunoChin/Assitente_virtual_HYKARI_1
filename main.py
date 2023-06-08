from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyttsx3
import core
from nlu.classifier import classify
import speech_recognition as sr

r = sr.Recognizer()
r.dynamic_energy_threshold = 1000

#Sinteze de voz
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
while True:

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        result = r.recognize_google(audio, language='pt-br')
        
    except sr.RequestError as e:
        result = r.recognize_vosk(audio, language='pt-br')
        result = json.loads(result)['text']
        
    except sr.UnknownValueError:
        continue
    
    if result != "" and len(str(result).split()) > 1:
        
        entity = classify(result)
            
        print(entity)
    
        if entity == "time|getTime":
            speak(core.SystemInfo.get_time())
        elif entity == "time|getDate":
            speak(core.SystemInfo.get_date())
        elif entity == "home|None":
            print(result)
