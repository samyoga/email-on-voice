#Python Email GUI Project by Dashvin Singh
#April 24 2017

from email import message_from_string
from tkinter import *
from tkinter import messagebox, Text
class Email():
    def __init__(self, username, password, cl):
        self._username = username
        self._password = password
        self._email = username
        self.client = {'UtorMail':['smtp.office365.com', 587], 'Gmail':['smtp.gmail.com', 587], 'Outlook':['smtp.live.com', 587], 'Yahoo':['smtp.mail.yahoo.com', 465]}
        import smtplib
        self.email_client=self.client[cl][0]
        self.port = self.client[cl][1]
        self.smtp = smtplib.SMTP(self.email_client, self.port)
        self.cl = cl
    def login(self):
        try:
            self.smtp.connect(self.email_client, self.port)
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.login(self._username, self._password)
            return True
##            from imaplib import IMAP4_SSL
##            self.imap = IMAP4_SSL('outlook.office365.com', 993)
##            self.imap.login(self._email, self._password)
##            print('IMAP Connection Successful')
        except:
            return False
    def send(self, to, subject='', message='', eom="Sent Using Python App"):
        new = "Subject: {0}\n{1} \n\n{2}".format(subject, message, eom)
        try:
            self.smtp.sendmail(self._email, to, new)
            return True
        except:
            return False

#Does not work yet
    def get_latest(self):
        self.imap.select('Inbox')
        result, data = self.imap.uid('search', None, 'ALL')
        latest_email_uid = data[0].split()[-1]
        result, data = self.imap.uid('fetch', latest_email_uid, '(BODY[TEXT])')
##        result, data = self.imap.search(None, "ALL")
##        ids = data[0] # data is a list.
##        id_list = ids.split() # ids is a space separated string
##        latest_email_id = id_list[-1] # get the latest
##        result, data = self.imap.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for th
        raw_email = data[0][1]
        raw_string = raw_email.decode('utf-8')
        message = message_from_string(raw_string)
        return message



class Email_GUI:
    def __init__(self, master, email):
        self.frame = Frame(master)
        master.title('Python Email, by DS')
        self.email = email
        master.minsize(width = 400, height = 400)
        master.config(bg = 'cyan')
        self.title = Label(master, text = 'Python Email', font = ("Century Gothic", 40), fg = 'black', bg = 'cyan')
        self.title.pack()
        text1 = 'This is a simple python application that is used to \nsend emails\
 with ease.'
        self.detail = Label(master, text = text1, font = ("Century Gothic", 15), fg = 'black', bg = 'cyan')
        self.detail.pack()
        self.connected = Label(master, text = '\nConnected to: {0}\n({1})\n'.format(self.email._username, self.email.cl), font = ("Century Gothic", 13), fg = 'red', bg = 'cyan')
        self.connected.pack()
        self.rec_title = Label(master, text = '\nReceiver Email Address', font = ("Century Gothic", 18), bg = 'cyan')
        self.rec_title.pack()
        self.notice = Label(master, text = 'Separate email addresses with a comma.', font = ("Century Gothic", 10), bg = 'cyan')
        self.notice.pack()
        self.rec_email = Entry(master, width = 40)
        self.rec_email.pack()
        self.sub_title = Label(master, text = '\nSubject', font = ("Century Gothic", 18), bg = 'cyan')
        self.sub_title.pack()
        self.text = Entry(master,width = 40)
        self.text.pack()
        self.text_title = Label(master, text = '\nMessage', font = ("Century Gothic", 18), bg = 'cyan')
        self.text_title.pack()
        self.main = Text(master, width = 50, height = 5)
        self.main.config(borderwidth=3)
        self.main.pack(ipady =3)
        self.send = Button(master, text = 'Send Email', command=self.send_email)
        self.send.pack()
        self.logout = Button(master, text = 'Logout', command=self.logout)
        self.logout.pack()
        self.master = master

    def send_email(self):
        rec = self.rec_email.get()
        
        if rec.lower() == 'myself':
            rec = self.email.username

        lst = rec.split()
        subj = self.text.get()
        mes = self.main.get(0.0, END)
        if self.verify_email(rec):
            send = messagebox.askyesno('Send Email?', 'Are you sure you want to send this email?\n\nSubject: {0}\n\nRecipient(s): {1}'.format(subj,rec))
            if bool(send) == True:
                for address in lst:
                    x = self.email.send(to = address, subject = subj, message = mes)
                if bool(x) == True:
                        messagebox.showinfo('Email Sent!', 'Congratulations! Successfully Sent Email!\n\nSubject: {0}\n\nRecipient(s): {1}'.format(subj,rec))
                else:
                    messagebox.showerror('Failed to Send email! Please Check your info')
        else:
            messagebox.showerror('Invalid Email address format!')


    def logout(self):
        x = messagebox.askyesno('Sign Out', 'Are you sure you want to log out?')
        if x:
            self.master.destroy()
            root = Tk()
            auth = Authentication(root)

    def verify_email(self, email):
        import re
        valid_re = re.compile(r'^.+@.+')
        if valid_re.match(email):
            return True
        else:
            return False




class Authentication:
    def __init__(self, master):
        self.frame = Frame(master)
        master.minsize(width = 200, height = 200)
        master.config(bg = 'cyan')
        master.title('Python Email Authentication')
        self.title = Label(master, text = 'Python Email Authentication', font = ("Century Gothic", 40), fg = 'black', bg = 'cyan')
        self.title.pack()
        text1 = 'Login to the email system! \nSupported Services: UtorMail, Gmail, Outlook, Yahoo'
        self.detail = Label(master, text = text1, font = ("Century Gothic", 15), fg = 'black', bg = 'cyan')
        self.detail.pack()
        #email Client
        self.variable = StringVar(master)
        self.variable.set('Choose One')
        self.w = OptionMenu(master, self.variable, 'Choose One', 'UtorMail', 'Gmail', 'Outlook', 'Yahoo')
        self.w.pack()
        #Username
        self.rec_title = Label(master, text = '\nEmail Address/Username', font = ("Century Gothic", 18), bg = 'cyan')
        self.rec_title.pack()
        self.rec_email = Entry(master, width = 40)
        self.notice = Label(master, text = 'Use your UtorMail if you wish you use the Uoft Servers', font = ("Century Gothic", 10), bg = 'cyan')
        self.rec_email.pack()
        self.notice.pack()
        #Password
        self.password_title = Label(master, text = '\nPassword', font = ("Century Gothic", 18), bg = 'cyan')
        self.password_title.pack()
        self.password_entry = Entry(master, show='*', width = 40)
        self.password_entry.pack()
        #button
        self.auth = Label(master, text = '\nAuthenticate', font = ("Century Gothic", 18), bg = 'cyan')
        self.auth.pack()
        self.button = Button(master, text='Authenticate', command = self.make_connection)
        self.button.pack()
        master.bind("<Return>", self.enter_key)
        self.master = master




    def make_connection(self):
        client = self.variable.get()
        if client == 'Choose One':
            messagebox.showerror('Invalid Email Client.' ,'Please choose a valid email client.')
        else:
            user = self.rec_email.get()
            password = self.password_entry.get()
            connect = Email(user, password, client)
            #print(client, user, password)
            x = connect.login()
            if x is not False and client is not 'Choose One':
                success = messagebox.showinfo('Connection Successful!',\
                                              'Connected to: \n{0}\nOK to proceed'.format(user))
                self.master.destroy()
                root = Tk()
                email_gui = Email_GUI(root, connect)
            else:
                messagebox.showerror('Connection Fail, try again',\
                                           "Invalid Username, Password, or Client, Please Try Again.")

    def enter_key(self, event):
        self.make_connection()

if __name__ == '__main__':
    root = Tk()
    auth = Authentication(root)
    root.mainloop()
