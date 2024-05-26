import resources

from time import sleep

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QSplashScreen

from windows.main_menu import MainMenu
from windows.settings_menu import SettingsWindow

import engine.render
import engine.manager

from utils.window_resize import runtime_resize

class WindowManager():

    def __init__(self):
        pass

    def run_splash(self):
        splash = QPixmap(":/icons/logo.jpg")
        splash_screen = QSplashScreen(splash)
        splash_screen.show()
        splash_screen.showMessage("Loading Assets", alignment=Qt.AlignBottom, color=Qt.white)
        sleep(1)
        splash_screen.showMessage("Loading Game", alignment=Qt.AlignBottom, color=Qt.white)
        sleep(0.5)
        self.main_menu = MainMenu()
        splash_screen.finish(self.main_menu)

    def open_menu(self):
        #self.main_menu = MainMenu() # this is only needed if you dereference it in open_settings
        self.main_menu.switch_window.connect(self.open_settings)
        self.main_menu.open_game.connect(self.load_game)
        self.main_menu.show()
        runtime_resize(self.main_menu)
        #self.settings_window = None # seems to resize fine without dereferencing

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.switch_window.connect(self.open_menu)
        self.settings_window.show()
        runtime_resize(self.settings_window)
        #self.main_menu = None

    def load_game(self):
        system = engine.manager.map_manage()
        map_texts = system.map_texts
        world_map = system.world_map
        cam = system.tony
        self.game_window = engine.render.my_house(160, 160, world_map, system, map_texts, cam)	      
        self.game_window.show()	
        self.main_menu.close()