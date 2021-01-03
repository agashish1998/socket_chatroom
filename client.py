import socket
import time



Header_size = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))


def crt_msg(msg, usr):
	l = len(msg)
	s = str(l)
	while len(s) < Header_size:
		s = '0' + s

	header = '|len|'+s + '|len||usr|'+ usr +"|usr|"+ "|strt|"	
	msg = header + msg
	m = msg + "|end|"
	m = bytes(m, 'utf-8')
	return m

def listen(usr):
	while True:
		msg = s.recv(1024)
		msg = str(msg)
		user_name = msg.split("|usr|")[1]
		msg = msg.split("|strt|")[1]
		msg = msg.split("|end|")[0]
		msg = msg.strip()

		print(" "+user_name+": "+msg, "\n>>>",  end="")
		time.sleep(1)

def sender(usr):
	while True:
		msg = input()
		msg = crt_msg(msg, usr)
		print("\n>>>",  end="")
		s.send(msg)


#s.close()



