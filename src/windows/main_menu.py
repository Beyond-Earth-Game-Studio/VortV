import resources
from datetime import date

from globals import fonts

from utils.logger import log
from utils.welcome import welcomemsg
from utils.window_resize import initial_resize

from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QTimer, QSettings, Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel

class MainMenu(QWidget):

    switch_window = Signal(None)
    open_game = Signal(None)

    def load_game(self):
        log("Game window opened", False)
        self.open_game.emit()
        self.close()

    def open_settings(self):
        log("Settings window opened", False)
        self.switch_window.emit()
        self.close()

    def exit(self):
        log("User requested exit", True)
        self.close()

    def __init__(self):

        super().__init__()

        # init variables
        title_font = fonts()[1]
        settings = QSettings("Beyond Earth Studios", "VortV")

        initial_resize(self, 'main menu')

        self.setWindowTitle("VortIV - Main Menu")
        self.setWindowIcon(QIcon(":/icons/logo.jpg"))
        self.setObjectName("MainMenu")

        layout = QVBoxLayout()
        
        layout.addSpacing(50)

        self.title = QLabel(welcomemsg())
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QFont(title_font, 30))
        layout.addWidget(self.title)

        play_button = QPushButton("Play")
        play_button.setFixedSize(400, 50)
        play_button.setObjectName("MenuButton")
        play_button.clicked.connect(self.load_game)
        layout.addWidget(play_button, alignment=Qt.AlignmentFlag.AlignCenter)

        settings_button = QPushButton("Settings")
        settings_button.setFixedSize(400, 50)
        settings_button.setObjectName("MenuButton")
        settings_button.clicked.connect(self.open_settings)
        layout.addWidget(settings_button, alignment=Qt.AlignmentFlag.AlignCenter)

        exit_button = QPushButton("Quit")
        exit_button.setFixedSize(400, 50)
        exit_button.setObjectName("MenuButton")
        exit_button.clicked.connect(self.exit)
        layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.copyright = QLabel(f'Copyright (c) {date.today().year} Beyond Earth Studios. All rights reserved.')
        self.copyright.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.copyright.setFont(QFont(title_font, 10))
        layout.addWidget(self.copyright)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.title_msg_refresh)
        self.timer.start(1000)

        self.setLayout(layout)

    def title_msg_refresh(self):
        self.title.setText(welcomemsg())