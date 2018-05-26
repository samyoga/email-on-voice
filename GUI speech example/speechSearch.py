from tkinter import ttk
from tkinter import *
import tkinter as tk
import webbrowser
import speech_recognition as sr
from pygame import mixer
import time

root = tk.Tk()
root.title('Universal search bar')
#root.iconbitmap('mic.ico')

style = ttk.Style()
#style.theme_use('winnative')

photo = PhotoImage(file='microphone.png').subsample(35, 35)

label1 = ttk.Label(root, text='Query')
label1.grid(row=0, column=0)

entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1, columnspan=4)

btn2 = tk.StringVar()

def callback():
    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'duck' and entry1.get() != '':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())
    elif btn2.get() == 'ytb' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())
    else:
        pass

def get(event):
    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'duck' and entry1.get() != '':
        webbrowser.open('https://duckduckgo.com/?q='+entry1.get())
    elif btn2.get() == 'ytb' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())
    else:
        pass

def buttonClick():
    mixer.init()
    mixer.music.load('chime1.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:
        try:
            s1 = time.time()*1000
            audio = r.listen(source, timeout=5)
            print(time.time()*1000-s1)
            # message = str(r.recognize_google(audio, key=""))
            start = time.time()*1000
            message = str(r.recognize_google(audio))
            print(time.time()*1000-start)
            mixer.music.load('chime2.mp3')
            mixer.music.play()
            entry1.focus()
            entry1.delete(0, END)
            entry1.insert(0, message)
            if btn2.get() == 'google':
                webbrowser.open('http://google.com/search?q='+message)
            elif btn2.get() == 'duck':
                webbrowser.open('http://duckduckgo.com/?q='+message)
            elif btn2.get() == 'ytb':
                webbrowser.open('https://www.youtube.com/results?search_query='+message)
            else:
                pass
        except sr.UnknownValueError:
            print('Google Speech Recognition could not Understand audio')
        except sr.RequestError as e:
            print('Could not request result from Google Speech Recogniser Service')
        else:
            pass

    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=6)

MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable = btn2)
MyButton2.grid(row=1, column=1, sticky=W)

MyButton3 = ttk.Radiobutton(root, text='Duck', value='duck', variable = btn2)
MyButton3.grid(row=1, column=2, sticky=W)

MyButton5 = ttk.Radiobutton(root, text='Youtube', value='ytb', variable = btn2)
MyButton5.grid(row=1, column=4, sticky=W)

MyButton6 = ttk.Button(root, image=photo, command=buttonClick)#, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton6.grid(row=0, column=5)

entry1.bind('<Return>', get)
entry1.focus()
root.wm_attributes('-topmost', 1)
btn2.set('google')
root.mainloop()