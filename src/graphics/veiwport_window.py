

import sys
import math
from PySide6.QtWidgets import QApplication,QGraphicsScene,QGraphicsView,QLabel,QGraphicsPixmapItem
from PySide6.QtGui import QImage,QPixmap

import camera

class my_house(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("my_house.wad")
        self.setScene(QGraphicsScene())  
        self.showMaximized()

    def keyPressEvent(self,event): # Take key input and change values. 
              
                key = event.key()
              
                self.cam.move(key)

    def set_cam(self,cam):
           self.cam = cam