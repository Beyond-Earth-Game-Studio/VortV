import sys
import math

from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage,QPixmap,QKeyEvent
from PySide6.QtWidgets import QGraphicsScene,QGraphicsView,QGraphicsPixmapItem,QWidget,QApplication

from graphics.VVAD_manager import VVAD
from graphics.camera import PlayerCamera
from graphics.render import RenderEngine

class EngineInstance():

    def __init__(self, data_path, viewport):
        super().__init__()

        # init class variables
        self.path = data_path
        self.viewport = viewport

        # non-scaled resolution
        self.screen_width = 225
        self.screen_height = 225
    
    def set_game_mode(self, mode):
       self.mode = mode
      
    def run(self):
        match self.mode:
            case "explore":
                self.explore_mode()
               
    def explore_mode(self):
        # setup viewport and set camera
        self.camera = PlayerCamera()
        self.viewport.set_camera(self.camera)
        self.viewport.showMaximized()
        self.viewport.setScene(QGraphicsScene())

        # get data from VVAD
        self.data = VVAD(self.path, self.camera)
        self.render_data = self.data.get_render_data()
        self.camera.set_camera_map(self.data.world_map)

        # setup rendering engine
        self.render_instance = RenderEngine(self.screen_width, self.screen_height, self.data.map_textures, self.data.world_map, self.camera, self.viewport, self.render_data)

        # setup refresh timer
        self.viewport.timer = QTimer(self.viewport)
        self.viewport.timer.start(0.1)
        self.viewport.timer.timeout.connect(self.refresh_render_instance)
    
    # clear scene, refresh and re-add new forground and background elements
    def refresh_render_instance(self):
            self.viewport.scene().clear()
            self.data.get_render_data()
            fg, bg = self.render_instance.tick_frame()
            self.viewport.scene().addPixmap(bg)
            self.viewport.scene().addItem(fg)
          
 
    

        

