import socket
from IPy import IP

ipaddress = input('[+] Enter Target To Scan: ')
port = 80

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print('[+] port 80 is open')
except:
    print('[-] Port 80 is Closed')