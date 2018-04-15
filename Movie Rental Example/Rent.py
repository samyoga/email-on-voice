__author__ = 'Bobby'
from tkinter import *
import webbrowser
import smtplib
import os
from PIL import ImageTk, Image
movies={"max payne":"https://www.youtube.com/watch?v=qHPFoD6Zpp8","legion":"https://www.youtube.com/watch?v=P6p01-in6-k",
        "22 jump street":"https://www.youtube.com/watch?v=rbZk_3KbRlg",
        "matrix":"https://www.youtube.com/watch?v=vKQi3bBA1y8"}
c=0
def signfunc():
    name=namez.get()
    password=passwordz.get()
    email=emailz.get()
    address=addressz.get()
    with open("user.txt",'a') as file:
        file.write(name)
        file.write("\n")
        file.write(password)
        file.write("\n")
        file.write(email)
        file.write("\n")
        file.write(address)
        file.write("\n")
    sam=Tk()
    sam.title("Thank you for signing up")
    gg=Label(text="Thanks you Sir!!")
    gg.grid(row=0,column=0)
    sam.mainloop()

def checklog():
    global c
    with open("user.txt") as f:
        data=f.readlines()
        for i in range(len(data)):
                nc=data[i].rstrip()
                if nc==lname.get():
                    pc=data[i+1].rstrip()
                if lname.get()==nc and lpass.get()==pc:
                    choosewin()
                    c=1
                    break


        if c==0:
            pk = Tk()
            pk.title("Wrong")
            ma=Label(pk,text="Wrong password or name")
            ma.grid(row=0,column=0)
            pk.mainloop()

def watch():
        webbrowser.open(movies[name11.get()])

def sendmail():
    tcost=0
    rcost=10
    check=name11.get()
    if check=="matrix" or check=="legion":
        tcost=200
    if check=="22 jump street" or check=="max payne":
        tcost=250
    tcost=int(rent.get())*rcost+tcost
    conn=smtplib.SMTP('smtp.gmail.com',587)
    conn.ehlo()
    conn.starttls()
    conn.login('gokuverma94@gmail.com',os.environ["pass"])
    conn.sendmail('gokuverma94@gmail.com',email11.get(),'Subject:Your Bill From Rental'
                                                                  '\n\nRespect Sir,\n'
                                                                  'Thank you for renting the movie '+check+
                  ' your total price is '+str(tcost)+'\n\nFrom Rental')
    conn.quit()

def mainwin():
    main = Tk()
    main.title("Movie Rental Application")
    img = ImageTk.PhotoImage(Image.open("a.jpg"))
    main.geometry("800x600+8+400")

    canvas=Canvas(main,width=470,height=80,relief='raised',borderwidth=3)
    canvas.grid(row=0,column=4,padx=80,pady=20)
    canvas.create_text(250,50,fill="green",font="Times 15 italic bold",
                            text="Please Login First, If you haven't then Signup.")

    text=Label(main,text="Welcome to Movie rental,enjoy movies and watch trailer too!",font="Times 15 italic bold")
    text.configure(bg="green",foreground="yellow")
    text.grid(row=1,column=4,padx=80,pady=40)
    panel = Label(main, image = img,height=220,width=600)
    panel.grid(row=3,column=4,padx=80,pady=20)
    frame=Frame(main)
    frame.grid(row=4,column=4,padx=50,pady=20)
    button1=Button(frame,text="Login",font="Times 10 italic bold",command=loginwin)
    button1.config( height =3, width = 15,bg="green")
    button1.grid(row=0,column=0,padx=50)
    button2=Button(frame,text="SignUp",font="Times 10 italic bold",command=signupwin)
    button2.config( height =3, width = 15,bg="yellow")
    button2.grid(row=0,column=1)
    main.mainloop()

def signupwin():
    global namez
    global passwordz
    global emailz
    global addressz
    signup = Tk()
    signup.title("Signup to movie rental")
    signup.geometry("800x600+8+400")
    canvas1=Canvas(signup,width=470,height=80,relief='raised',borderwidth=1)
    canvas1.grid(row=0,column=4,padx=80,pady=20)
    canvas1.create_text(250,50,fill="red",font="Times 15 italic bold",
                            text="Provide geniune information for billing purpose")

    text1=Label(signup,text="Fill the below provided fields",font="Times 15 italic bold")
    text1.configure(bg="brown",foreground="white")
    text1.grid(row=1,column=4,padx=60,pady=40)

    frame1=Frame(signup)
    frame1.grid(row=2,column=4,pady=20)
    panel1 = Label(frame1,text="Enter your name:",font="Times 13 italic bold")
    panel1.grid(row=0,column=0,pady=20)
    panel1.configure(foreground="black")
    panel2 = Label(frame1,text="Enter your password:",font="Times 13 italic bold")
    panel2.grid(row=1,column=0,pady=20)
    panel2.configure(foreground="black")
    panel3 = Label(frame1,text="Enter your Email id:",font="Times 13 italic bold")
    panel3.grid(row=2,column=0,pady=20)
    panel3.configure(foreground="black")
    panel4 = Label(frame1,text="Enter your address:",font="Times 13 italic bold")
    panel4.grid(row=3,column=0,pady=20)
    panel4.configure(foreground="black")

    frame2=Frame(signup)
    frame2.grid(row=2,column=5,pady=20)
    namez=Entry(frame2)
    namez.grid(row=0,column=0,pady=20)
    passwordz=Entry(frame2,show="#")
    passwordz.grid(row=1,column=0,pady=20)
    emailz=Entry(frame2)
    emailz.grid(row=2,column=0,pady=20)
    addressz=Entry(frame2)
    addressz.grid(row=3,column=0,pady=20)

    button3=Button(signup,text="Signup!",font="Times 10 italic bold",command=signfunc)
    button3.config( height =3, width = 15,bg="green")
    button3.grid(row=3,column=4,padx=50)
    signup.mainloop()

def loginwin():
    login = Tk()
    login.title("Login to Movie rental")
    login.geometry("600x400+8+400")
    global lname
    global lpass
    text2=Label(login,text="Fill the below provided fields",font="Times 15 italic bold")
    text2.configure(bg="black",foreground="white")
    text2.grid(row=1,column=4,padx=60,pady=40)

    frame3=Frame(login)
    frame3.grid(row=2,column=4,pady=20)
    panel11 = Label(frame3,text="Enter your name:",font="Times 13 italic bold")
    panel11.grid(row=0,column=0,pady=20)
    panel11.configure(foreground="black")
    panel21 = Label(frame3,text="Enter your password:",font="Times 13 italic bold")
    panel21.grid(row=1,column=0,pady=20)
    panel21.configure(foreground="black")

    frame4=Frame(login)
    frame4.grid(row=2,column=5,pady=20)
    lname=Entry(frame4)
    lname.grid(row=0,column=0,pady=20)
    lpass=Entry(frame4,show="#")
    lpass.grid(row=1,column=0,pady=20)

    button4=Button(login,text="Login!",font="Times 10 italic bold",command=checklog)
    button4.config( height =3, width = 15,bg="green")
    button4.grid(row=3,column=4,padx=50)
    login.mainloop()

def choosewin():
    choose = Tk()
    choose.title("Rent your movie")
    choose.geometry("800x600+8+400")
    global name11
    global email11
    global rent
    text3=Label(choose,text="Welcome sir please go ahead and rent your movie",font="Times 15 italic bold")
    text3.configure(bg="black",foreground="white")
    text3.grid(row=0,column=4,padx=60,pady=40)
    framez=Frame(choose)
    framez.grid(row=1,column=4,pady=20)
    panel1z = Label(framez,text="Currently available movies:-",font="Times 13 italic bold")
    panel1z.grid(row=0,column=0,pady=5)
    panel112 = Label(framez,text="Matrix",font="Times 13 italic bold")
    panel112.grid(row=1,column=0,pady=5)
    panel113 = Label(framez,text="Legion",font="Times 13 italic bold")
    panel113.grid(row=2,column=0,pady=5)
    panel114 = Label(framez,text="Max Payne",font="Times 13 italic bold")
    panel114.grid(row=3,column=0,pady=5)
    panel115 = Label(framez,text="22 Jump Street",font="Times 13 italic bold")
    panel115.grid(row=4,column=0,pady=5)
    frame31=Frame(choose)
    frame31.grid(row=2,column=4,pady=15)
    panel11 = Label(frame31,text="Enter the name of your movie:",font="Times 13 italic bold")
    panel11.grid(row=0,column=0,pady=15)
    panel11.configure(foreground="black")
    panel21 = Label(frame31,text="Enter your email for billing purpose:",font="Times 13 italic bold")
    panel21.grid(row=1,column=0,pady=15)
    panel21.configure(foreground="black")
    panel22 = Label(frame31,text="Enter the time for rent:",font="Times 13 italic bold")
    panel22.grid(row=2,column=0,pady=15)
    panel22.configure(foreground="black")
    frame41=Frame(choose)
    frame41.grid(row=2,column=5,pady=15)
    name11=Entry(frame41)
    name11.grid(row=0,column=0,pady=15)
    email11=Entry(frame41)
    email11.grid(row=1,column=0,pady=15)
    rent=Entry(frame41)
    rent.grid(row=2,column=0,pady=20)
    button41=Button(choose,text="Rent Now",font="Times 11 italic bold",command=sendmail)
    button41.config( height =3, width = 15,bg="red")
    button41.grid(row=3,column=4,padx=50)
    button41=Button(choose,text="Watch Trailer",font="Times 11 italic bold",command=watch)
    button41.config( height =3, width = 15,bg="red")
    button41.grid(row=3,column=5)
    choose.mainloop()

mainwin()
