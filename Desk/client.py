import socket
import sys
import msvcrt

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'portNo please'
port = input();
print 'ip please'
address = raw_input();
server_address = (address, port)

print 'Connecting to the server'

sock.connect(server_address)

try:
    char  = msvcrt.getche();
    while (char!='q'):
        sock.sendall(char)
        print char
        char  = msvcrt.getche();
    sock.sendall(char)

finally:
    print 'closing'
    sock.close()
            
