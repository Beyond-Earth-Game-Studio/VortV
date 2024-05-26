import resources
from datetime import date

from globals import fonts
from utils.logger import log
from utils.welcome import welcomemsg
from utils.window_check import check
from utils.window_resize import initial_resize, runtime_resize
from windows.settings_menu import SettingsWindow

from PySide6.QtCore import Qt, QTimer, QSettings
from PySide6.QtGui import QIcon, QFont, QFontDatabase
from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel

class MainMenu(QWidget):

    def load_game(self):
        log("Game window opened", False)
        self.maingame = Game()
        self.maingame.show()
        runtime_resize(self.maingame)
        self.close()

    def open_settings(self):
        log("Settings window opened", False)
        self.settings_window = SettingsWindow()
        self.settings_window.show()
        #runtime_resize(self.settings_window)

    def exit(self):
        self.settings_window = SettingsWindow()
        self.settings_window.close()
        self.close()

    def refresh(self):
        self.label.setText(welcomemsg())

    def __init__(self):

        super().__init__()

        # init variables
        forced = check()
        title_font = fonts()[1]
        settings = QSettings("Beyond Earth Studios", "VortV")

        # Ensure opening of new windows
        #self.settings_window = None
        #self.maingame = None

        initial_resize(self, 'main menu')

        self.setWindowTitle("VortIV - Main Menu")
        self.setWindowIcon(QIcon(":/icons/logo.jpg"))
        self.setObjectName("MainMenu")

        layout = QVBoxLayout()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

        layout.addSpacing(50)

        self.label = QLabel(welcomemsg())
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont(title_font, 30))
        layout.addWidget(self.label)

        button = QPushButton("Play")
        button.setFixedSize(400, 50)
        button.setObjectName("MenuButton")
        button.clicked.connect(self.load_game)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        button2 = QPushButton("Settings")
        button2.setFixedSize(400, 50)
        button2.setObjectName("MenuButton")
        button2.clicked.connect(self.open_settings)
        layout.addWidget(button2, alignment=Qt.AlignmentFlag.AlignCenter)

        button3 = QPushButton("Quit")
        button3.setFixedSize(400, 50)
        button3.setObjectName("MenuButton")
        button3.clicked.connect(self.exit)
        layout.addWidget(button3, alignment=Qt.AlignmentFlag.AlignCenter)

        self.copyright = QLabel(f'Copyright (c) {date.today().year} Beyond Earth Studios. All rights reserved.')
        self.copyright.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.copyright.setFont(QFont(title_font, 10))
        layout.addWidget(self.copyright)

        self.setLayout(layout)

