import resources

from globals import fonts
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

    def open_menu(self):
        log("Menu window opened", False)
        self.switch_window.emit()
        self.close()

    def window_size(self, size):

        primary_font = fonts()[0]

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

        forced = check(False)

        if forced:
            center(self)  # seems to screw with autoscale on linux
            log("Centering window", False)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirm")
        dlg.setText("Confirm Changes?")
        dlg.setFont(QFont(primary_font, 10))
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        dlg.show()
        center(dlg)
        confirm = dlg.exec()

        if confirm == QMessageBox.Yes and forced:
            log(f'Size change confirmed: {size}', True)
            settings.setValue("geometry", self.geometry())
            settings.setValue("forced size", 1)
            settings.setValue("target size", size)
            center(self)
            settings.setValue("resized", 1)

        if confirm == QMessageBox.Yes and not forced:
            log("Size change confirmed: Autoscale", True)
            settings.setValue("forced size", 0)
            settings.setValue("target size", "Autoscale")
            settings.setValue("resized", 1)

        if confirm == QMessageBox.No:
            log("Size change cancelled", True)
            self.setGeometry(settings.value("geometry"))
            center(self)

    def __init__(self):

        super().__init__()

        forced = check(False)
        primary_font = fonts()[0]
        log_level = settings.value("log_level")

        initial_resize(self, 'settings window')

        self.setWindowTitle("VortIV - Settings")
        self.setWindowIcon(QIcon(":/icons/logo.jpg"))
        self.setObjectName("SettingsWindow")
        layout = QVBoxLayout()
        box_layout = QVBoxLayout()
        box2_layout = QVBoxLayout()

        box = QGroupBox("Force Display Size")

        display = QComboBox()
        display.addItems(["", "Default (Autoscale)", "700x450", "1920x1080", "2880x1800", "3840x2160"])
        display.setFont(QFont(primary_font, 10))
        display.currentTextChanged.connect(self.window_size)
        box_layout.addWidget(display)

        box.setLayout(box_layout)
        layout.addWidget(box)

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
