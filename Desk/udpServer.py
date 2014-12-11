import socket
import MouseFunctions as mouse

UDP_IP = "43.0.212.32"
UDP_PORT = 10005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
	data, addr = sock.recvfrom(1)
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
	else:
		continue
