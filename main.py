import os  # system commands
import smtplib  # smtp protocol
import time  # time parameters

import pyaudio  # portaudio bindings
import pyttsx3  # OFFLINE Python Text to Speech library
import speech_recognition as sr  # Library for speech recognition

'''
Initialize sr and speech-engine
'''
r = sr.Recognizer()
engine = pyttsx3.init()

'''
Microphone receive value of email
'''
with sr.Microphone(device_index= None) as source: #Start microphone for email input
    r.adjust_for_ambient_noise(source) #noise cancellation
    engine.say("Email id") # Speaker -> Enter email id?
    engine.runAndWait() #Loop for email id enter
    time.sleep(5) # time interval for value like delay in microprocessor
    audio = r.listen(source) # Listen to microphone source input
    time.sleep(3) # timer
    engine.say("Got it!") #Fetched the id
    engine.runAndWait() #loop

command = r.recognize_google(audio) #Google-recognizition API call for Audio
command = command.replace(" ", "") #seperation of username and domain

'''
Speaker says that following user will receive the email
'''
describe = "Sending message to" + command 
engine.say(describe)
engine.runAndWait()

server = smtplib.SMTP('smtp.gmail.com', 587) #Gamil host with portname
server.starttls() #to TLS mode
server.login("Your Email ID", "Your password") #Email id of the sender where Your Email ID = exp@exp.com && Your password = exp123

'''
Speaker send out info to enter the message then the microphone will start to receive the text
'''
with sr.Microphone(device_index= None) as source:
    r.adjust_for_ambient_noise(source)
    engine.say("Message to be sent")
    engine.runAndWait()
    time.sleep(5)
    audio = r.listen(source)
    engine.say("Got it!")
    engine.runAndWait()

msg = r.recognize_google(audio) # Run Speech to text on message
print (msg) # Show received message

server.sendmail("Your Email ID", command, msg) #Send mail with values for message and receiver id where Your Email ID = exp@exp.com
server.quit() # Quit server
