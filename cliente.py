#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket


s=socket.socket()
s.connect(("127.0.0.1",1234))
s.send([5,10,0,28,90,10])
s.close()