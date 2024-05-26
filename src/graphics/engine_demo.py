import engine

import sys
from PySide6.QtWidgets import QApplication

import  veiwport_window


if __name__ == '__main__':
    app = QApplication(sys.argv)
 
    viewport = veiwport_window.my_house()
    active_engine = engine.engine_instance("data/world_sections.csv",viewport)
    active_engine.set_game_mode("explore")
    active_engine.run_engine()
    
    app.exec()

