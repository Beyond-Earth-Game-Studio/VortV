
import math
from PySide6.QtWidgets import QGraphicsScene,QGraphicsView,QGraphicsPixmapItem,QWidget,QApplication
from PySide6.QtGui import QImage,QPixmap,QKeyEvent
from PySide6.QtCore import QTimer
import render
import sys
import  render,veiwport_window
import VVAD_manager,camera

class engine_instance():
    def __init__(self,data_path,veiwport):
        super().__init__()
        self.mode = "explore"
        self.screen_width = 225
        self.screen_height = 225
        self.path = data_path
        self.veiwport = veiwport
        
    
    def set_game_mode(self,mode):
       self.mode = mode
      
    def run_engine(self):
        match self.mode:
            case "explore":
                self.init_explore()
               
    def init_explore(self):
        
        self.cam = camera.player_camera()
        self.data = VVAD_manager.VVAD(self.path,self.cam)
        self.cam.set_cam_geo(self.data.world_map)
        self.veiwport.setScene(QGraphicsScene())  
        self.veiwport.showMaximized()
        self.render_data = self.data.get_render_data()
       
        self.veiwport.set_cam(self.cam)
        self.graphics = render.render_engine(self.screen_width, self.screen_height,self.data.map_texts,self.data.world_map,self.cam,self.veiwport,self.render_data)
        self.veiwport.timer = QTimer(self.veiwport)
        self.veiwport.timer.start(0.1)
        self.veiwport.timer.timeout.connect(self.connect_to_render)
        
        
    def connect_to_render(self):
            self.veiwport.scene().clear()
            self.data.get_render_data()
            fg,bg = self.graphics.tick_frame()
            self.veiwport.scene().addPixmap(bg)
            self.veiwport.scene().addItem(fg)
          
 
    

        

