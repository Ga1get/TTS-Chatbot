import os
import time
import playsound
import webbrowser
import speech_recognition as sr
from gtts import gTTS
from factoring import factorMachine

name = ''

fctr = factorMachine

def speak(text):
        tts = gTTS(text=text, lang="en",tld='ca')
        filename = "testEnvTTS.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            #print("Exception: " + str(e))
            time.sleep(1)

    return said



    

    

def process(text):

        if "what are the factors of " in text: #factoring requests
            for i in text.split():
                if i.isdigit():
                    holder = int(i)
                    print(fctr.factoringProcess(holder))
            return


        if "what is your name" in text:
            speak("My name is "+ name + " TTS version 1")
            time.sleep(1)
            return

        if "what's your name" in text:
            speak("My name is "+ name + " TTS version 1")
            time.sleep(1)
            return

        if "monkey" in text:
            speak("GOD I LOVE MONKEYS")
            time.sleep(1)   
            return

        if "what's the best food from Lonestar" in text:
            speak("Obviously its the cabo taco, you imbecile")
            time.sleep(1)
            return
        
        if "switch mode" in text:   #opening Brawlhalla
            os.startfile("C:/Users/Colin/Desktop/2NDPANAL.bat")
            return
        
        if "full-screen desktop mode" in text:   #opening Brawlhalla
            os.startfile("C:/Users/Colin/Desktop/2NDPANALextend.bat")
            return

        if "open brawlhalla" in text:   #opening Brawlhalla
            os.startfile("F:/Steam1tb/steamapps/common/Brawlhalla/Brawlhalla.exe")
            return
        
        if "open Rocksmith" in text:    #opening Rocksmith
            os.startfile("D:\SteamLibrary\steamapps\common\Rocksmith2014\Rocksmith2014.exe")
            return

        if "open DS emulator" in text:    #opening Rocksmith
            os.startfile("C:/Users/Colin/Desktop/DS Emulator/DeSmuME_0.9.11_x64.exe")
            return
        
        if "open crunchyroll" in text:  #Opening crunchyroll
            url = "https://www.crunchyroll.com/videos/anime"
            webbrowser.get().open(url)
            speak("Enjoy!")
            return

        if "search YouTube" in text:    #Youtube search
            speak("What would you like to search for?")
            search = getAudio()
            url = "https://www.youtube.com/results?search_query=" + search
            webbrowser.get().open(url)
            speak("Heres what I found for " + search + " on YouTube")
            return

        if "search Wikipedia" in text:  #wiki search
            speak("What would you like to search for?")
            search = getAudio()
            url = "https://en.wikipedia.org/wiki/" + search
            webbrowser.get().open(url)
            speak("Heres what I found for " + search + " on Wikipedia")
            return
        
        if "search" in text:    #Search engine search
            speak("What would you like to search for?")
            search = getAudio()
            url = "https://google.com/search?q=" + search
            webbrowser.get().open(url)
            speak("Heres what I found for " + search)
            return