from socket import *
import sys
try:
    s=socket(AF_INET, SOCK_STREAM)
    print('socket created sucessfully')
except socket.error as err:
    print('socket creation faile with erroe {err}')
try:
    host_ip=gethostbyname('www.github.com')
    # print(host_ip)
except gaierror:
    print('error resolving the host')
    sys.exit()
port=80
s.connect((host_ip,port))
print(f'socket successfully connected to git hub on ip =={host_ip} port {port} ')