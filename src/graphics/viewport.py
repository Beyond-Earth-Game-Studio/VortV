from PySide6.QtWidgets import QGraphicsScene, QGraphicsView

class my_house(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("my_house.wad")
        self.setScene(QGraphicsScene())  
        self.showMaximized()

    # Take key input and change values
    def keyPressEvent(self, event):  
        key = event.key()
        self.cam.move(key)

    def set_cam(self, cam):
           self.cam = cam