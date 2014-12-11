import socket
import sys
import MouseFunctions as mouse

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'portNo please'
port = input();
print 'ip please'
address = raw_input();
server_address = (address, port)
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
            data = connection.recv(1)
            if data:
                print data
            if data=='w':
                mouse.move(0,-10)
            elif data=='a':
                mouse.move(-10,0)
            elif data=='d':
                mouse.move(10,0)
            elif data=='s':
                mouse.move(0,10)
            elif data=='p':
                mouse.press()
            elif data=='c':
                mouse.click()   
            elif data=='r':
                mouse.release()
            elif data=='o':
                mouse.rPress()
            elif data=='x':
                mouse.rClick()   
            elif data=='t':
                mouse.rRelease()
            elif data=='q':
                print 'close received'
                break;
            else:
                continue
            
    finally:
        # Clean up the connection
        print 'Closing Connection'
        connection.close()
        
