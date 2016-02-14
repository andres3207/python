#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
#from PyQt5.QtGlobal import *
#import socket


class Ventana(QWidget):

    def __init__(self, *args): 
        QWidget.__init__(self, *args)

        self.setGeometry(0,0,1366, 768)
        self.setWindowTitle('Titulo de ventana')
        label = QLabel('Zona de dibujo')
        layout = QVBoxLayout()
        layout.addWidget(label)

        self.vista=QGraphicsView()
        self.vista.setFixedSize(1440,900)
        self.escena=QGraphicsScene()
        self.vista.setScene(self.escena)
        layout.addWidget(self.vista)
        self.setLayout(layout)

        self.timer1=QTimer()
        print("inicio socket")
        self.socket=QTcpSocket()
        self.server=QTcpServer()
        self.server.listen(QHostAddress.Any,1234)
        print("Listening")
        self.server.newConnection.connect(self.aceptarConexion)
        self.timer1.timeout.connect(self.timer1Timeout)


        self.dibujar(3,2)


    def dibujar(self,x,y):
    	self.escena.addLine(x,y,x,y)
    	#self.escena.addLine(10,10,10,10)
    def aceptarConexion(self):
    	print("Se ha conectado un cliente")
    	self.socket=self.server.nextPendingConnection()
    	self.timer1.setInterval(1000)
    	self.timer1.start()
    def timer1Timeout(self):
    	print("timeout")
    	datos=self.socket.readAll()
    	n=datos.size()
    	i=0
    	while i<n:
    		x=datos.at(i)
    		y=datos.at(i+1)
    		i=i+2
    		print("X: "+x+" Y: "+y)
    		self.dibujar(int(x),int(y))
    	#print(n)

    def timerEvent(self,QTimerEvent):
    	print("Timer")





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ventana()
    ex.show()
    sys.exit(app.exec_())