from socket import *
from datetime import datetime
s=socket(AF_INET,SOCK_DGRAM)
addr=('192.168.56.1', 6666)
text=f"The time is {datetime.now()}"
myformat='ascii'
data=text.encode(myformat)
s.sendto(data,addr)
print(f'The os assigned me the address {s.getsockname()}')
data, address=s.recvfrom(1024)
text=data.decode(myformat)
print(f"The server at {address} replied '{text}'")
# print('The server at {} replied {!r}'.format(address,text))
#===============================================================================
from socket import *
from datetime import datetime
s=socket(AF_INET,SOCK_DGRAM)
addr=('192.168.56.1', 6666)
text=f"The time is {datetime.now()}"
myformat='ascii'
data=text.encode(myformat)
s.connect(addr)
while True:
    s.send(data)
    print(f'The os assigned me the address {s.getsockname()}')
    delay=.1
    s.settimeout(delay)
    try:
        data =s.recv(1024)
    except socket.timeout as exc:
        delay*=2
        if delay>2:
            print(f'error is {exc}')
text=data.decode(myformat)
print(f"The server at {address} replied '{text}'")

