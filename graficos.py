#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Ventana(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,1366, 768)
        self.setWindowTitle('Titulo de ventana')
        label = QLabel('Zona de dibujo')
        layout = QVBoxLayout()
        layout.addWidget(label)
        #layout.setAlignment(Qt.AlignCenter)
        self.vista=QGraphicsView()
        self.vista.setFixedSize(1440,900)
        self.escena=QGraphicsScene()
        self.vista.setScene(self.escena)
        layout.addWidget(self.vista)
        self.setLayout(layout)
        zzz=self.vista.geometry;
        #print(type(zzz))
        #print("X: "+zzz+", Y: "+zzz)
        self.dibujar()

    def dibujar(self):
    	self.escena.addLine(-683,-384,683,384)
    	self.escena.addLine(-683,384,683,-384)
    	zzz=self.vista.geometry;
    	#print("X: "+zzz+", Y: "+zzz)


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    ex = Ventana()
    ex.show()
    sys.exit(app.exec_())