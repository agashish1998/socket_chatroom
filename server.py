import socket
import time
import threading

Header_size = 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = input("please enter the ip address:")
ip_address = ip_address.strip()
port = int(input("please input port number:"))
s.bind((ip_address, port))
s.listen(4)
print("server is listening...")
clients = []

def handle_command(data, cli):
	msg = extract_msg(data).strip()
	msg = msg[1:]
	msg = msg.strip()
	if (msg == "quit"):
		cli.close()
		clients.remove(cli)
	if (msg == "ping"):
		cli.send(crt_msg("hi", "server"))



def broadcast_data(cli, data):
	msg = data
	for  c in clients:
		if c != cli or not cli:
			c.sendall(data)
	
def extract_msg(msg):
	msg = msg.decode()
	msg = msg.split("|msg|")[1]
	return msg

def extract_user_name(msg):
	msg = msg.decode()
	user_name = msg.split("|usr|")[1]
	return user_name

def extract_len_msg(msg):
	msg = msg.decode()
	l = msg.split("|len|")[1]
	return int(l)


def crt_msg(msg, usr_name):
	l = len(msg) +  2*len("|len|") + 2*len("|usr|") + 2*len("|msg|") + Header_size + len(usr_name)
	s = str(l)
	while len(s) < Header_size:
		s = '0' + s

	header = '|len|'+s + '|len||usr|'+ usr_name +"|usr|"+ "|msg|"	
	msg = header + msg
	m = msg + "|msg|"
	m = bytes(m, 'utf-8')
	return m
	
def new_connection():
	global s, clients
	while True:
		conn, addr = s.accept()
		clients.append(conn)
		print("connection established with {}".format(addr))
		t = threading.Thread(target=listen_msgs, args=(conn,))
		t.start()

		
def listen_msgs(cli):
	global s, clients
	
	try:
		while True:
			data = cli.recv(100)
			print(data)
			data_len = extract_len_msg(data)
			print("data length is {}".format(data_len))
			while len(data) < data_len:
				temp = cli.recv(100).decode()
				data = data + temp
				#print("data inside the second while loop")
				#print(temp)
				#print(len(data))
			print("------------------------------------------------------------------")
			msg = extract_msg(data).strip()
			if msg[0] == ":":
				handle_command(data, cli)
			else:
				broadcast_data(cli, data)
			time.sleep(0.1)
	except Exception as e:
		print("client disconnceted due to following error: {}".format(str(e)))
		clients.remove(cli)
		print(len(clients))
		

t1 = threading.Thread(target= new_connection)
t1.start()





#s.close()







#while True:
#	clientsocket, address = s.accept()
#	print('connection established to {}'.format(address))
#	
#	if clientsocket not in clients:
#		clients.append(clientsocket)
#	
#	










