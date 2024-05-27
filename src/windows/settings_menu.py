import resources

from globals import fonts, index_check

from utils.logger import log
from utils.window_check import check
from utils.window_center import center
from utils.window_resize import initial_resize

from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSettings, Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QRadioButton, QComboBox, QMessageBox, \
    QGroupBox

settings = QSettings("Beyond Earth Studios", "VortV")

class SettingsWindow(QWidget):

    switch_window = Signal(None)

    def open_menu(self):
        log("Menu window opened", False)
        self.switch_window.emit()
        self.close()

    def set_log(self):

        if self.sender().text() == "Verbose" and self.sender().isChecked():
            if self.sender().text() != settings.value("log_level"):
                log("Setting log level to 'Verbose' - will take effect on next restart", True)
            settings.setValue("log_level", "Verbose")

        if self.sender().text() == "Warn" and self.sender().isChecked():
            if self.sender().text() != settings.value("log_level"):
                log("Setting log level to 'Warn' - will take effect on next restart", True)
            settings.setValue("log_level", "Warn")

        if self.sender().text() == "Error" and self.sender().isChecked():
            if self.sender().text() != settings.value("log_level"):
                log("Setting log level to 'Error' - will take effect on next restart", True)
            settings.setValue("log_level", "Error")

    def window_size(self, size):

        if settings.value("geometry") is None:
            settings.setValue("geometry", self.geometry())

        if size == "Default (Autoscale)":
            log("Size set to Autoscale", True)
            self.showMaximized()
            settings.setValue("forced size", 0)

        if size == "700x450":
            log("Size set to 700x450", True)
            self.resize(700, 450)
            settings.setValue("forced size", 1)

        if size == "1920x1080":
            log("Size set to 1920x1080", True)
            self.resize(1920, 1080)
            settings.setValue("forced size", 1)

        if size == "2880x1800":
            log("Size set to 2880x1800", True)
            self.resize(2880, 1800)
            settings.setValue("forced size", 1)

        if size == "3840x2160":
            log("Size set to 3840x2160", True)
            self.resize(3840, 2160)
            settings.setValue("forced size", 1)

        if self.forced:
            center(self)  # seems to screw with autoscale on linux
            log("Centering window", False)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirm")
        dlg.setText("Confirm Changes?")
        dlg.setFont(QFont(self.primary_font, 10))
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        dlg.show()
        center(dlg)
        confirm = dlg.exec()

        if confirm == QMessageBox.Yes and self.forced:
            log(f'Size change confirmed: {size}', True)
            settings.setValue("geometry", self.geometry())
            settings.setValue("forced size", 1)
            settings.setValue("target size", size)
            center(self)
            settings.setValue("resized", 1)
            settings.setValue("Size Index", self.display.currentIndex())
            print(settings.value("Size Index"))

        if confirm == QMessageBox.Yes and not self.forced:
            log("Size change confirmed: Autoscale", True)
            settings.setValue("forced size", 0)
            settings.setValue("target size", "Autoscale")
            settings.setValue("resized", 1)
            settings.setValue("Size Index", self.display.currentIndex())
            print(settings.value("Size Index"))

        if confirm == QMessageBox.No:
            log("Size change cancelled", True)
            self.setGeometry(settings.value("geometry"))
            center(self)

    def resolution(self, scale):

        old_scale = settings.value("scale")

        if scale == "Ultra":
            log("Scale set to Ultra", True)
            settings.setValue("scale", (350, 350))

        if scale == "High":
            log("Scale set to High", True)
            settings.setValue("scale", (250, 250))

        if scale == "Medium":
            log("Scale set to Medium", True)
            settings.setValue("scale", (200, 200))

        if scale == "Low":
            log("Scale set to Low", True)
            settings.setValue("scale", (150, 150))

        if scale == "HP_Destroyer_696969":
            log("Scale set to HP_Destroyer_696969", True)
            settings.setValue("scale", (50, 50))

        forced = check(False)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirm")
        dlg.setText("Confirm Changes?")
        dlg.setFont(QFont(self.primary_font, 10))
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        dlg.show()
        center(dlg)
        confirm = dlg.exec()

        if confirm == QMessageBox.Yes:
            log(f'Scale change confirmed: {settings.value("scale")}', True)
            settings.setValue("Scale Index", self.display2.currentIndex())
            print(settings.value("Scale Index"))

        if confirm == QMessageBox.No:
            log("Scale change cancelled", True)
            settings.setValue("scale", old_scale)

    def __init__(self):

        super().__init__()

        index = index_check()
        self.forced = check(False)
        self.primary_font = fonts()[0]
        log_level = settings.value("log_level")

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
        self.display.addItems(["", "Default (Autoscale)", "700x450", "1920x1080", "2880x1800", "3840x2160"])
        self.display.setFont(QFont(self.primary_font, 10))
        self.display.setCurrentIndex(index[0])
        self.display.currentTextChanged.connect(self.window_size)
        box_layout.addWidget(self.display)

        box.setLayout(box_layout)
        layout.addWidget(box)

        box1 = QGroupBox("Render Scale")

        self.display2 = QComboBox()
        self.display2.addItems(["", "Ultra", "High", "Medium", "Low", "HP_Destroyer_696969"])
        self.display2.setFont(QFont(self.primary_font, 10))
        self.display2.setCurrentIndex(index[1])
        self.display2.currentTextChanged.connect(self.resolution)
        box1_layout.addWidget(self.display2)

        box1.setLayout(box1_layout)
        layout.addWidget(box1)

        box2 = QGroupBox("Log Level", self)
        radio1 = QRadioButton("Verbose", self)
        radio2 = QRadioButton("Warn", self)
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
