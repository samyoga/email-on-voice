#!/usr/local/bin/python

try:
    import Tkinter
except ImportError:
    import tkinter as Tkinter
import time
import threading
import random
import queue
import socket
import sys
from datetime import datetime

class GuiPart:
    def __init__(self, master, queue):
        self.queue = queue
        # GUI stuff
        self.labelArray = []
        self.messages = []
        # Set up the GUI
        self.master = master
        self.backgroundColor = 'black'
        self.listsize = 10
        master.config(bg=self.backgroundColor)
        self.board = Tkinter.LabelFrame(self.master, text='Notification Board',     bg='Black', fg='Yellow', labelanchor='n', width=170)
        self.initLabels()
        self.board.pack()

    def initLabels(self) :
        self.textColorTime = 'cyan'
        self.textColorMessage = 'orange'
        colorTime = 'blue'
        colorMessage = 'red'
        for i in range(0,self.listsize):
            la = Tkinter.Label(self.board, height=0, width=10, bg=self.backgroundColor, fg=colorTime, anchor=Tkinter.W)
            lb = Tkinter.Label(self.board, height=0, width=160, bg=self.backgroundColor, fg=colorMessage)
            la.grid(row=i,column=0, sticky=Tkinter.W)
            lb.grid(row=i,column=1, sticky=Tkinter.W)
            self.labelArray.append((la, lb))
            colorTime = self.textColorTime
            colorMessage = self.textColorMessage
            self.initList()
        self.displayList()

    def initList(self):
        for i in range(0, self.listsize):
            t = ''
            m = ''
            self.messages.append((t,m))

    def processIncoming(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.processMessage(msg)
            except Queue.Empty:
                pass

    def processMessage(self, message):
        timestamp = datetime.utcnow().strftime('%H:%M:%S')
        self.publish(timestamp, message)

    def publish(self, msg1, msg2):
        self.addToList(msg1, msg2)
        self.displayList()

    def addToList(self, msg1, msg2):
        if len(self.messages) == self.listsize:
            self.messages.pop(0)
        if (msg1 == None):
            msg1 = datetime.utcnow().strftime('%H:%M:%S')
        newMessage = (msg1, msg2)
        self.messages.append(newMessage)

    def displayList(self):
        index = self.listsize -1
        for t, m in self.messages :
            la, lb = self.labelArray[index]
            la.config(text=t)
            lb.config(text=m)
            index = index -1

    def destroy(self):
        self.master.destroy()

class ThreadedClient:

    def __init__(self, master):
        self.master = master
        # Create the queue
        self.queue = queue.Queue()
        # Define connection parameters
        self.conn = None
        self.bindError = False
        # Set up the GUI part
        self.gui = GuiPart(master, self.queue)
        # Set up the thread to do asynchronous I/O
        self.running = True
        self.commThread = threading.Thread(target=self.workerThreadReceive)
        self.commThread.daemon = True
        self.commThread.start()
        # Start the periodic call in the GUI to check if the queue contains anything
        self.periodicCall()

    def periodicCall(self):
        if not self.running:
            self.killApplication()
        else :
            self.gui.processIncoming()
            self.master.after(100, self.periodicCall)

    def workerThreadReceive(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try :
            s.bind((HOST, PORT))
        except socket.error as msg :
            #print 'Bind failed. Error code: ' + str(msg[0]) + ' Error message: ' + str(msg[1])
            self.running = False
            self.bindError = True
            return
        s.listen(1)
        (self.conn, self.addr) = s.accept()
        while self.running :
            data = self.conn.recv(1024)
            if data == 'Q' :
                self.conn.sendall('Q')
                self.running = False
            else :
                self.queue.put(data)
                reply = 'ACK'
                self.conn.sendall(reply)
        if self.conn is not None:
            self.conn.close()

    def killApplication(self):
        self.running = False
        if (self.conn is None) and (not self.bindError) :
            sfake = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sfake.connect((HOST,PORT))
            sfake.sendall('Q')
            sfake.close()
        self.gui.destroy()
        sys.exit()


HOST = ''       # Symbolic name meaning the local host
PORT = 24073    # Arbitrary non-privileged port

root = Tkinter.Tk()

client = ThreadedClient(root)

root.protocol("WM_DELETE_WINDOW", client.killApplication)
root.mainloop()