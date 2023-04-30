from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyttsx3
import core

#Sinteze de voz
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

model = Model("model_pt-br")
recoginizer = KaldiRecognizer(model, 16000)

cap     = pyaudio.PyAudio()
stream  = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

while True:
    data = stream.read(2048)
    if len(data) == 0:
       break
    if recoginizer.AcceptWaveform(data):
        result = recoginizer.Result()
        result = json.loads(result)
        
        if result['text'] is not None:
            text = result['text']
        
            print(text)
            
            if text == 'que horas são' or text == 'me diga as horas':
                speak(core.SystemInfo.get_time())
        
