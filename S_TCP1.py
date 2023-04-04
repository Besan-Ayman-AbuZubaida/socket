from socket import *
server_ip=gethostbyname(gethostname())
print(server_ip)
port=56789
s=socket(AF_INET,SOCK_STREAM)
# s.bind(('192.168.56.1',port))
s.bind(('',port))
s.listen(5)
print(f'server listenting at {server_ip} port {port}')
while True:
    conn,add=s.accept()
    print(f'connect with client at {add}')
    msg='Thanks for connecting'
    conn.send(msg.encode("utf-8"))
    conn.close()
