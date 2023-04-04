# from socket import *
# s=socket(AF_INET,SOCK_DGRAM)
# server_ip=gethostbyname(gethostname())
# port=6666
# s.bind((server_ip,port))
# print(f'listening at {s.getsockname()}')
# while True:
#     data,addr=s.recvfrom(1024)
#     myformat='ascii'
#     text= data.decode(myformat)
#     print(f"The client at {addr} says '{text}'")
#     text=f'your data was {len(data)} bytes long'
#     data=text.encode(myformat)
#     s.sendto(data, addr)

#==================================================================
from socket import *
from random import random
s=socket(AF_INET,SOCK_DGRAM)
server_ip=gethostbyname(gethostname())
port=6666
s.bind((server_ip,port))
print(f'listening at {s.getsockname()}')
while True:
    data,addr=s.recvfrom(1024)
    if random()<.5:
        print(f'pretending to drop packets from {addr}')
        continue
    myformat='ascii'
    text= data.decode(myformat)
    print(f"The client at {addr} says '{text}'")
    text=f'your data was {len(data)} bytes long'
    data=text.encode(myformat)
    s.sendto(data, addr)
