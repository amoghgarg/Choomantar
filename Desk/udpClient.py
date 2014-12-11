import socket
import msvcrt

UDP_IP = "43.0.212.32"
UDP_PORT = 10005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((UDP_IP,UDP_PORT))

try:
	char  = msvcrt.getche();
	while (char!='q'):
		sock.send(char)
		print char
		char  = msvcrt.getche();
	sock.sendto(char)
finally:
	print 'closing'
	sock.close()