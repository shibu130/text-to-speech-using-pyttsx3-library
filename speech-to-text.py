import pyttsx3
from sys import exit
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


while(True):

    text=input("enter to speak   q:exit   \n")
    if text=="q":
        print("exiting....")
        break
    
    engine.say(text)
    engine.runAndWait()
  
 
