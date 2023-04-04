from socket import *
server_ip='192.168.56.1'
port=6666
myformat='utf-8'
s=socket(AF_INET,SOCK_STREAM)
s.connect((server_ip,port))
print('HEllooooo')
while True:
    data=s.recv(1024)
    if not data:
        break
    print(f'data recieved from server: {data.decode(myformat)}')
s.close()