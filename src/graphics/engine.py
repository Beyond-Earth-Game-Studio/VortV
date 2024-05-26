
import math
from PySide6.QtWidgets import QGraphicsScene,QGraphicsView,QGraphicsPixmapItem,QWidget,QApplication
from PySide6.QtGui import QImage,QPixmap,QKeyEvent
from PySide6.QtCore import QTimer
import render
import sys
import  render,veiwport_window
import VVAD_manager,camera

class engine():
    def __init__(self,data_path):
        super().__init__()
        self.mode = "explore"
        self.screen_width = 225
        self.screen_height = 225
        self.path = data_path
        
        
        
    
    #def set_game_mode(self,mode):
       # self.mode = mode
      
    def run_engine(self):
        match self.mode:
            case "explore":
                self.explore()
               
    def init_explore(self):
        
        self.cam = camera.player_camera()
        self.data = VVAD_manager.VVAD(self.path,self.cam)
        self.cam.set_cam_geo(self.data.world_map)
        viewport.setScene(QGraphicsScene())  
        viewport.showMaximized()
        self.render_data = self.data.get_render_data()
       
        viewport.set_cam(self.cam)
        self.graphics = render.render_engine(self.screen_width, self.screen_height,self.data.map_texts,self.data.world_map,self.cam,viewport,self.render_data)
        viewport.timer = QTimer(viewport)
        viewport.timer.start(0.1)
        viewport.timer.timeout.connect(self.connect_to_render)
        
        
    def connect_to_render(self):
            viewport.scene().clear()
            self.data.get_render_data()
            fg,bg = self.graphics.tick_frame()
            viewport.scene().addPixmap(bg)
            viewport.scene().addItem(fg)
          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("yo")
    viewport = veiwport_window.my_house()
    engine_instance = engine("data/world_sections.csv")
    engine_instance.init_explore()
    sys.exit(app.exec())	 
    
