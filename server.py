import socket,random,smtplib
from email.message import EmailMessage
class app:
	file_name = "database.txt"
	def __init__(self,ip,port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((ip, port))
		s.listen(5)
		self.conn, self.addr = s.accept()
		print(self.addr, " has connected") 
		while True:
			info = self.conn.recv(1024).decode('utf-8')
			info = info.split(",")
			if info[0] == 'l':
				self.login(info[1],info[2])
			elif info[0] == 'r':
				self.register(info[1],info[2],info[3])
	def register(self, username, password, email):
		with open(self.file_name, "a") as w:
			w.write(username + "," + password + "," + email + "\n")		
	def login(self, username, password):
		with open(self.file_name, "r+") as r:
			info = r.read()	
		info = info.split("\n")
		self.login_bool = False
		for i in info:
			x = i.split(",")
			if x[0] == username and x[1] == password:
				 self.login_bool = True
		self.conn.send(b"Login" if self.login_bool == True else b"Error")
app = app('127.0.0.1', 52000)