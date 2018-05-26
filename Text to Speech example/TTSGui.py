from tkinter import *
import pyttsx3 as pyttsx
engine=pyttsx.init()


def sRate():
   voices=engine.getProperty('voices')
   engine.setProperty('voice',voices[1].id)
    
def male():
   voices=engine.getProperty('voices')
   engine.setProperty('voice',voices[0].id)
   
def female():
   voices=engine.getProperty('voices')
   engine.setProperty('voice',voices[2].id)   
   
   
def speak():
    text_entered=textentry.get()
    engine.say(text_entered)
    engine.runAndWait()
def exit_program():
    window.destroy()
    exit()

    
    
window=Tk()


window.configure(background="black")
window.title("Text to Speech Program")
Label(window,text="Enter text",bg="black", fg="white",font="Arial 16 bold").grid(row=0,column=0,sticky=W)
textentry=Entry(window,width=20,bg="white")
textentry.grid(row=1,column=0,sticky=W)
Button(window,text="Submit",width=6,command=speak).grid(row=2,column=0,sticky=W)
Label(window,text="Click to close",bg="black",fg="white",font="Arial 12 underline").grid(row=3,column=0,sticky=W)
Label(window,text="Gender",bg="black",fg="white",font="Arial 12 underline").grid(row=0,column=3,sticky=E)
Button(window,text="Male",width=6,command=male).grid(row=3,column=2,sticky=E)
Button(window,text="Female",width=6,command=sRate).grid(row=3,column=3,sticky=E)
Button(window,text="Female 2",width=6,command=female).grid(row=3,column=4,sticky=E)



Button(window,text="Close",width=6,command=exit_program).grid(row=4,column=0,sticky=W)


window.mainloop()

