import os #system commands
import smtplib #smtp protocol
import time #time parameters

import pyaudio #portaudio bindings
import pyttsx3 #OFFLINE Python Text to Speech library
import speech_recognition as sr #Library for speech recognition

'''
Initialize sr ans speech-engine
'''
r = sr.Recognizer()
engine = pyttsx3.init()
with sr.Microphone(device_index= None) as source: #Start microphone for email input
        r.adjust_for_ambient_noise(source) #noise cancellation
        engine.say("Email id") # Speaker -> Enter email id?
        engine.runAndWait() #Loop for email id enter
        time.sleep(5) # time interval for value like delay in microprocessor
        audio = r.listen(source) # Listen to microphone source input
        time.sleep(3) # timer
        engine.say("Got it!") #Fetched the id
        engine.runAndWait() #loop