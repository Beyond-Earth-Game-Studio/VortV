import sys
import math

from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage,QPixmap,QKeyEvent
from PySide6.QtWidgets import QGraphicsScene,QGraphicsView,QGraphicsPixmapItem,QWidget,QApplication

import graphics.render as render, graphics.viewport as viewport, graphics.VVAD_manager as VVAD_manager, graphics.camera as camera

class engine_instance():

    def __init__(self, data_path, viewport):
        super().__init__()

        self.path = data_path
        self.mode = "explore"

        # non-scaled resolution
        self.screen_width = 225
        self.screen_height = 225

        self.viewport = viewport
        
    def set_game_mode(self, mode):
       self.mode = mode
      
    def run(self):
        match self.mode:
            case "explore":
                self.explore_mode()
               
    def explore_mode(self):
        self.cam = camera.player_camera()
        self.data = VVAD_manager.VVAD(self.path,self.cam)
        self.cam.set_cam_geo(self.data.world_map)
        self.viewport.setScene(QGraphicsScene())  
        self.viewport.showMaximized()
        self.render_data = self.data.get_render_data()
       
        self.viewport.set_cam(self.cam)
        self.graphics = render.render_engine(self.screen_width, self.screen_height, self.data.map_textures, self.data.world_map, self.cam, self.viewport, self.render_data)
        self.viewport.timer = QTimer(self.viewport)
        self.viewport.timer.start(0.1)
        self.viewport.timer.timeout.connect(self.connect_to_render)
        
    def connect_to_render(self):
            self.viewport.scene().clear()
            self.data.get_render_data()
            fg, bg = self.graphics.tick_frame()
            self.viewport.scene().addPixmap(bg)
            self.viewport.scene().addItem(fg)
          
 
    

        

