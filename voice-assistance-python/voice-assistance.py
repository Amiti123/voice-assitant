


import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjoke
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Try to speak....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("not understable....")

def speechtx():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    # 0=male voice  1=female voice
    rate=engine.getProperty('rate',150)
    engine.say(x)
    engine.runAndWait()


# sptext()
# speechtx(" hello welcom back ")
    
if __name__ =='__main__':
        if "hey siri" in sptext().lower() :
          while True:
              data1=sptext().lower()

              if "your  name" in data1:
                name = "my name is siri"
                speechtx(name)

            
                  
              elif "old are you" in data1:

    
          
          

          
               age = "i am two yers old"
               speechtx(age)

          elif 'now time' in data1:
             time=datetime.datetime.now().strftime("%I%M%p")
             speechtx(time)

          elif 'youtube' in data1:
             webbrowser.open("link of youtube")

          elif "joke" in data1:
               joke_1 = pyjokes.get_joke(language="en", category="neutral")
               print(joke_1)
               speechtx(joke_1)

          elif 'play song' in data1:
                add = "address\\"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[0]))


            # 0 for index number

          elif "exit" in data1:
            speechtx("thank you")
            break
          
          time.sleep(5)







    else:
        print("")



