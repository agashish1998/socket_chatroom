import client
import threading

usr = 'ashish'
#password = 'asdf'

Header_size = 5

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 1234))
print(">>>",  end="")


t1 = threading.Thread(target=client.listen, args=[usr])
t2 = threading.Thread(target=client.sender, args=[usr])
t1.start()
t2.start()

#s.close()





#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('192.168.0.8', 1234))
#s.listen(4)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#	s.connect(('192.168.0.8', 1234))
#	s.send(bytes('hello chat', 'utf-8'))
#	time.sleep(3)
#	s.send(bytes('its client1', 'utf-8'))
