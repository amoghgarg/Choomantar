import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10005)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:            
            print "Waiting for data"
            data = connection.recv(16)
            if data:
                print >>sys.stderr, 'received "%s"' % data
                connection.sendall(data)
            else:                
                break
            
    finally:
        # Clean up the connection
        connection.close()
        print 'Closing Connection'
