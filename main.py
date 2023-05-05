import os
import speech_recognition as sr
import pyttsx3,pywhatkit,wikipedia
from pyrae import dle

nombre = "Juan"
listener = sr.Recognizer()
micro = sr.Microphone()
engine =pyttsx3.init()

voice = engine.getProperty('voices') 
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate',150)

print("Programa iniciado.")


def hablar(text):
    engine.say(text)
    engine.runAndWait()

def escuchar():
    try:
        with micro as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc,language='es')
            rec = rec.lower()
            if nombre in rec:
                rec = rec.replace(nombre,'')
    except:
        pass
    return rec

def run():
    while True:
        engine.setProperty('rate',150)
        rec = escuchar()
        if 'buscar' in rec:
            busqueda = rec.replace('buscar','')
            print("Buscando "+busqueda)
            hablar("Buscando "+busqueda)
            pywhatkit.search(busqueda)
        elif 'definir' in rec:
            busqueda = rec.replace('definir','')
            print("Buscando "+busqueda)
            hablar("Buscando "+busqueda)
            res = dle.search_by_word(word=busqueda)
            print(res)
            hablar(res)
        elif 'wikipedia' in rec:
            engine.setProperty('rate',100)
            busqueda = rec.replace('wikipedia','')
            print("Buscando "+busqueda)
            hablar("Buscando "+busqueda)
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(busqueda,1)
            print(wiki)
            hablar(wiki)
        elif 'apagar' in rec:
            hablar("Apagando computadora.")
            print("Apagando computadora")
        elif 'salir' in rec:
            hablar("Cerrando programa.")
            exit()

if __name__ == '__main__': 
    run()





