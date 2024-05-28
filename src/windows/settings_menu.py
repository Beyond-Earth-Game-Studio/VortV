import resources

from globals import fonts, index_check, screen_size_check

from utils.window_check import check
from utils.dialog import create_dialog
from utils.window_center import center
from utils.logger import log, change_log
from utils.window_resize import initial_resize

from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSettings, Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QRadioButton, QComboBox, QMessageBox, QGroupBox

settings = QSettings("Beyond Earth Studios", "VortV")

class SettingsWindow(QWidget):

    switch_window = Signal(None)

    def open_menu(self):
        log("Menu window opened", False)
        self.switch_window.emit()
        self.close()

    def __init__(self):

        super().__init__()

        self.index = index_check()
        self.primary_font = fonts()[0]
        log_level = settings.value("Log_Level")

        initial_resize(self, 'settings window')

        self.setWindowTitle("VortIV - Settings")
        self.setWindowIcon(QIcon(":/icons/logo.jpg"))
        self.setObjectName("SettingsWindow")

        layout = QVBoxLayout()
        box_layout = QVBoxLayout()
        box1_layout = QVBoxLayout()
        box2_layout = QVBoxLayout()

        box = QGroupBox("Force Display Size")

        self.display = QComboBox()
        self.display.addItems(["Default (Maximized)", "Tiny", "Small", "Medium", "Large"])
        self.display.setFont(QFont(self.primary_font, 10))
        self.display.setCurrentIndex(self.index[0])
        self.display.currentTextChanged.connect(self.window_size)
        box_layout.addWidget(self.display)

        box.setLayout(box_layout)
        layout.addWidget(box)

        box1 = QGroupBox("Render Scale")

        self.display2 = QComboBox()
        self.display2.addItems(["Ultra", "High", "Medium", "Low", "HP_Destroyer_696969"])
        self.display2.setFont(QFont(self.primary_font, 10))
        self.display2.setCurrentIndex(self.index[1])
        self.display2.currentTextChanged.connect(self.resolution)
        box1_layout.addWidget(self.display2)

        box1.setLayout(box1_layout)
        layout.addWidget(box1)

        box2 = QGroupBox("Log Level")
        radio1 = QRadioButton("Verbose")
        radio2 = QRadioButton("Warn")
        radio3 = QRadioButton("Error")
        radio1.toggled.connect(self.set_log)
        radio2.toggled.connect(self.set_log)
        radio3.toggled.connect(self.set_log)

        if log_level == "Verbose":
            radio1.setChecked(True)

        if log_level == "Warn":
            radio2.setChecked(True)

        if log_level == "Error":
            radio3.setChecked(True)

        box2_layout.addWidget(radio1)
        box2_layout.addWidget(radio2)
        box2_layout.addWidget(radio3)

        box2.setLayout(box2_layout)
        layout.addWidget(box2)

        button = QPushButton("Return to Main Menu")
        button.setFixedSize(400, 50)
        button.setObjectName("MenuButton")
        button.clicked.connect(self.open_menu)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def set_log(self):

        selected_log_level = self.sender().text()
        box_is_checked = self.sender().isChecked()

        change_log(selected_log_level, box_is_checked)

    def window_size(self, size: str):

        # debating where to put this... 
        if settings.value("geometry") is None:
            settings.setValue("geometry", self.geometry())

        if size == "Default (Maximized)":
            log("Size set to Autoscale", True)
            self.showMaximized()
            settings.setValue("Is_Forced_Size", 0)

        if size == "Tiny":
            self.resize(screen_size_check()[0] / 3, screen_size_check()[1] / 3)
            log(f'Size set to {self.geometry().width()}x{self.geometry().height()} (Tiny)', True)
            settings.setValue("Is_Forced_Size", 1)

        if size == "Small":
            self.resize(screen_size_check()[0] / 2, screen_size_check()[1] / 2)
            log(f'Size set to {self.geometry().width()}x{self.geometry().height()} (Small)', True)
            settings.setValue("Is_Forced_Size", 1)

        if size == "Medium":
            self.resize(screen_size_check()[0] / 1.5, screen_size_check()[1] / 1.5)
            log(f'Size set to {self.geometry().width()}x{self.geometry().height()} (Medium)', True)
            settings.setValue("Is_Forced_Size", 1)

        if size == "Large":
            self.resize(screen_size_check()[0] / 1.25, screen_size_check()[1] / 1.25)
            log(f'Size set to {self.geometry().width()}x{self.geometry().height()} (Large)', True)
            settings.setValue("Is_Forced_Size", 1)

        forced = check(False) # this needs to be here to poll for changes.. duh

        if forced:
            center(self)  # seems to screw with autoscale on linux
            log("Centering window", False)

        confirm = create_dialog(self)

        if confirm == QMessageBox.Yes and forced:
            log(f'Size change confirmed: {self.geometry().width()}x{self.geometry().height()}', True)
            settings.setValue("Window_Geometry", self.geometry())
            settings.setValue("Is_Forced_Size", 1)
            settings.setValue("Target_Size", f'{self.geometry().width()}x{self.geometry().height()}')
            settings.setValue("Resized_During_Runtime", 1)
            settings.setValue("Size_Index", self.display.currentIndex())
            center(self)


        if confirm == QMessageBox.Yes and not forced:
            log("Size change confirmed: Autoscale", True)
            settings.setValue("Is_Forced_Size", 0)
            settings.setValue("Target_Size", "Autoscale")
            settings.setValue("Resized_During_Runtime", 1)
            settings.setValue("Size_Index", self.display.currentIndex())

        if confirm == QMessageBox.No:
            log("Size change cancelled", True)
            self.display.blockSignals(True)
            self.display.setCurrentIndex(self.index[0])
            self.display.blockSignals(False)
            self.setGeometry(settings.value("Window_Geometry"))
            center(self)

    def resolution(self, scale: str):

        old_scale = settings.value("Render_Scale")

        if scale == "Ultra":
            log("Scale set to Ultra", True)
            settings.setValue("Render_Scale", 350)

        if scale == "High":
            log("Scale set to High", True)
            settings.setValue("Render_Scale", 250)

        if scale == "Medium":
            log("Scale set to Medium", True)
            settings.setValue("Render_Scale", 200)

        if scale == "Low":
            log("Scale set to Low", True)
            settings.setValue("Render_Scale", 150)

        if scale == "HP_Destroyer_696969":
            log("Scale set to HP_Destroyer_696969", True)
            settings.setValue("Render_Scale", 50)

        confirm = create_dialog(self)

        if confirm == QMessageBox.Yes:
            log(f'Render scale change confirmed: {settings.value("Render_Scale")}', True)
            settings.setValue("Scale_Index", self.display2.currentIndex())

        if confirm == QMessageBox.No:
            log("Render scale change cancelled", True)
            self.display2.blockSignals(True)
            self.display2.setCurrentIndex(self.index[1])
            self.display2.blockSignals(False)
            settings.setValue("Render_Scale", old_scale)