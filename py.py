import random
import sys
import pyttsx3
def speak(audio):
    engine=pyttsx3.init()
    voice=engine.getProperty("voices")
    engine.setProperty("voice",voice[1].id)
    engine.setProperty("rate",110)
    engine.setProperty("volume",500)
    engine.say(audio)
    engine.runAndWait()
ask_again="yes"
while (ask_again=="yes"):
  if(ask_again=="no"):
    exit()
  ans=random.randint(0,8)
  question=input("ENTER YOUR QUESTION: ")
  if(ans==0):
    speak("smart work matters")
  elif(ans==1):
    speak("that might not be the correct way")
  elif(ans==2):
    speak("repeat again!")
  elif(ans==3):
    speak("work hard you will achieve!")
  elif(ans==4):
    speak("be active and work on it")
  elif(ans==5):
    speak("be concentrated you will achieve")
  elif(ans==6):
    speak("ups and down's are common in life")
  elif(ans==7):
    speak("be patient you will definitely win")
  elif(ans==8):
    print("only one life be happy ")
  ask_again=input("click yes to ask again:")
