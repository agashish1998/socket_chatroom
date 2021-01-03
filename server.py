import socket
import time
import threading

Header_size = 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(4)

clients = []

def broadcast_data(cli, data):
	msg = data
	for  c in clients:
		if c != cli or not cli:
			c.sendall(data)
	

def crt_msg(msg):
	l = len(msg)
	s = str(l)
	while len(s) < Header_size:
		s = '0' + s
		
	header = '|len|'+s + '|len||usr|'+ usr +"|usr|"+ "|strt|"	
	msg = header + msg
	m = msg + "|end|"
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
	
	while True:
		data = str(cli.recv(100))
		data_len = data.split('|len|')[1]
		print("data length is {data_len}")
		data_len = int(data_len)
		while len(data) < data_len:
			data = data + str(cli.recv(100))
		print("received data from a client")
		broadcast_data(cli, bytes(data, "utf-8"))
		time.sleep(1)
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










