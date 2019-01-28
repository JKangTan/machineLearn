from socket import *
from time import ctime

HOST = ""
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock =socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


while True:
	print("wating for connection...")
	tcpCliSock, addr = tcpSerSock.accept()
	print("...connection from :" , addr)

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break 
		tcpCliSock.send('[%s] %s'%(ctime(), data.decode('utf-8')))

	tcpCliSock.close()
tcpSerSock.close()
