#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import random

print("Ejecucion de programa")
s=socket.socket()
s.connect(("127.0.0.1",1234))
i=0
while i<10000000:
	X=random.randrange(0,1366)
	Y=random.randrange(0,768)
	mensaje=str(X)+','+str(Y)+'\n'
	#print(bytes(mensaje, 'utf-8'))
	s.send(bytes(mensaje, 'utf-8'))
	i=i+1
s.send(b'2000,2000\n')
#s.send(b'10,77\n')
#s.send(b'0,77\n')
#s.send(b'28,77\n')
#s.send(b'90,77\n')
#s.send(b'10,77\n')
#s.send([5,10,0,28,90,10])
s.close()


