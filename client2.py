import client
import threading

usr = 'ankit'
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


