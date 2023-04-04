from socket import *
server_ip=gethostbyname(gethostname())
print(server_ip)
port=6666
myformat='utf-8'
s=socket(AF_INET,SOCK_STREAM)
s.bind((server_ip,port))
s.listen(5)
conn, add=s.accept()
msg=input('Enter msg to be send to client')
while msg.lower().strip()!='exit':
    conn.sendall(msg.encode(myformat))
    print('Data is sent')
    msg=input('Enter msg to be send to client')

conn.close()