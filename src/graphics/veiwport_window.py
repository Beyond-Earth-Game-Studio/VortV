

import sys
import math
from PySide6.QtWidgets import QApplication,QGraphicsScene,QGraphicsView,QLabel,QGraphicsPixmapItem
from PySide6.QtGui import QImage,QPixmap


class my_house(QGraphicsView):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.setWindowTitle("my_house.wad")
        self.setScene(QGraphicsScene())  
        self.showMaximized()

              
    