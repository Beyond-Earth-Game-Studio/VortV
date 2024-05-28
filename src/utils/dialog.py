from globals import fonts
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMessageBox
#from utils.window_center import center

def create_dialog(self):
    dlg = QMessageBox(self)
    dlg.setWindowTitle("Confirm")
    dlg.setText("Confirm Changes?")
    dlg.setFont(QFont(self.primary_font, 10))
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setIcon(QMessageBox.Question)
    dlg.show()
    #center(dlg) # seems to be not needed? will test on windows later
    response = dlg.exec()

    return response