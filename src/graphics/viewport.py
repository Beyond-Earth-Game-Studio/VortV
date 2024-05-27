import resources
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView

class MyHouse(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(":/icons/logo.jpg"))
        self.setWindowTitle("my_house.wad")
        self.setScene(QGraphicsScene())  
        self.showMaximized()

    # Take key input and change values
    def keyPressEvent(self, event):  
        key = event.key()
        self.cam.move(key)

    def set_camera(self, cam):
           self.cam = cam