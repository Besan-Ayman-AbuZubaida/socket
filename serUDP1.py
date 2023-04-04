# from socket import *
# IP_add=gethostbyname(gethostname())
# port=6666
# myformat='utf-8'
# s=socket(AF_INET,SOCK_DGRAM) 
# s.bind((IP_add,port))
# data, addr=s.recvfrom(1024)
# print(f'data recieved is {data.decode(myformat)}')
# msg='Hello from server to client'
# s.sendto(msg.encode(myformat),addr)
# s.close()


#===================================================================

from socket import *
def sum(num1,num2):
    return(num1+num2)

IP_add=gethostbyname(gethostname())
port=6666
myformat='utf-8'
s=socket(AF_INET,SOCK_DGRAM) 
s.bind((IP_add,port))
# try:
#     add, port=s.getsockname()
#     print(f'add is {add} port is {port}')
# except OSError as e:
#     print(f"Error binding socket: {e}")
data1, addr=s.recvfrom(1024)
data2, addr=s.recvfrom(1024)
print(sum(int(data1),int(data2)))
msg=sum(int(data1),int(data2))
s.sendto(str(msg).encode(myformat),addr)
s.close()