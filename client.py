import socket
import time
import threading

usr = input("your name: ")
#password = 'asdf'

Header_size = 5

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 1234))

Header_size = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = input("please enter the ip address:")
ip_address = ip_address.strip()
port = int(input("please input port number:"))
s.connect((ip_address, port))
print(">>>",  end="")


def crt_msg(msg, usr):
	l = len(msg) +  2*len("|len|") + 2*len("|usr|") + 2*len("|msg|") + Header_size + len(usr)
	s = str(l)
	while len(s) < Header_size:
		s = '0' + s

	header = '|len|'+s + '|len||usr|'+ usr +"|usr|"+ "|msg|"	
	msg = header + msg
	m = msg + "|msg|"
	m = bytes(m, 'utf-8')
	#print("sending this message {} \n with length {}".format(str(m), len(m)))
	return m

def listen(usr):
	while True:
		msg = s.recv(1024)
		msg = msg.decode()
		data_len = msg.split('|len|')[1]
		#print("data length is {}".format(data_len))
		data_len = int(data_len)
		while len(msg) < data_len:
			temp = cli.recv(100).decode()
			msg = msg + temp
		user_name = msg.split("|usr|")[1]
		msg = msg.split("|msg|")[1]

		print(" "+user_name+": "+msg, "\n>>>",  end="")
		time.sleep(1)

def sender(usr):
	while True:
		msg = input()
		msg = crt_msg(msg, usr)
		print("\n>>>",  end="")
		s.send(msg)
t1 = threading.Thread(target=listen, args=[usr])
t2 = threading.Thread(target=sender, args=[usr])
t1.start()
t2.start()

#s.close()



