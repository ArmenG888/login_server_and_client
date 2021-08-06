from tkinter import *
from tkinter import messagebox
from functools import partial
import smtplib
from email.message import EmailMessage
import random, socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(("127.0.0.1", 52000))
class app:
	login_bool = False
	def __init__(self, root):
		self.root = root
		login_button = Button(root, text="Login",command=self.loginentry).pack()
		register_button = Button(root, text="Register", command=self.registerentry).pack() 
	def loginentry(self):
		loginwindow = Toplevel()
		Label(loginwindow, text="Username or Email").pack()
		self.username = Entry(loginwindow)
		self.username.pack()
		Label(loginwindow, text="Password").pack()
		self.password = Entry(loginwindow, show="*")
		self.password.pack()
		Button(loginwindow, text="Login",command=self.login).pack()
	def registerentry(self):
		registerwindow = Toplevel()
		Label(registerwindow, text="Username").pack()
		self.username = Entry(registerwindow)
		self.username.pack()
		Label(registerwindow, text="Email").pack()
		self.email = Entry(registerwindow)
		self.email.pack()
		Label(registerwindow, text="Password").pack()
		self.password = Entry(registerwindow, show="*")
		self.password.pack()
		Label(registerwindow, text="Repeat Password").pack()
		self.repeat_password = Entry(registerwindow, show="*")
		self.repeat_password.pack()
		self.Checkbutton1 = IntVar()  
		Button(registerwindow, text="Register", command=self.register).pack()
	def register(self):
		username = self.username.get()
		email = self.email.get()
		password = self.password.get()
		repeat_password = self.repeat_password.get()
		if password == repeat_password:
			s.send(b"r" +b","+ username.encode('utf-8') + b"," + password.encode('utf-8') + b"," + email.encode('utf-8'))
			messagebox.showinfo("register", "Your account has successfully been created")
		else:
			messagebox.showwarning("Error", "Passwords are not matching")
	def login(self):
		username = self.username.get()
		password = self.password.get()
		s.send(b"l"+b","+ username.encode('utf-8') + b"," +password.encode('utf-8'))
		login_recv = s.recv(1024).decode('utf-8')
		login_recv = login_recv.split(",")
		if login_recv[0] == "Error":
			messagebox.showerror("Error", "Passwords or Username is wrong!")
		elif login_recv[0] == "Login":
			messagebox.showinfo("Login", "You have successfully logged into your account:)")		
			self.change_login_bool()
	@classmethod
	def change_login_bool(cls):
		cls.login_bool = True
root = Tk()
app1 = app(root)
mainloop()
