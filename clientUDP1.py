# from socket import *
# IP_add=gethostbyname(gethostname())
# port=6666
# mytuple=(IP_add,port)
# myformat='utf-8'
# s=socket(AF_INET,SOCK_DGRAM) 
# msg='Hello from client to server'
# s.sendto(msg.encode(myformat),mytuple)
# data, addr=s.recvfrom(1024)
# print(data.decode(myformat))
# s.close()
#========================================
from socket import *
IP_add=gethostbyname(gethostname())
port=6666
mytuple=(IP_add,port)
myformat='utf-8'
s=socket(AF_INET,SOCK_DGRAM) 
num1=int(input('Enter 1st num: '))
num2=int(input('Enter 2nd num: '))
# msg='Hello from client to server'
msg1=str(num1)
s.sendto(msg1.encode(myformat),mytuple)
msg2=str(num2)
s.sendto(msg2.encode(myformat),mytuple)
data, addr=s.recvfrom(1024)
print(f'sum is {data.decode(myformat)}')
s.close()
