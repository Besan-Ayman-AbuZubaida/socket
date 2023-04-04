from socket import *
s=socket()
s.connect(('192.168.56.1',56789))
data=s.recv(1024)
print(data.decode("utf-8"))
s.close()
