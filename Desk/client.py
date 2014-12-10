import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10005)

print 'Connecting to the server'

sock.connect(server_address)

try:
    mess = 'Some'
    for i in range(1,5):
        sock.sendall(mess)

        rec = 0;
        rec_exp  = len(mess)

        
        data = sock.recv(16)
        rec_exp += len(data)
        print rec
        print rec_exp
        print data

finally:
    print 'closing'
    sock.close()
            
