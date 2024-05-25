import sys
import resources

from time import sleep
from datetime import datetime

from utils.style import stylize
from utils.logger import logging_init, logging_exit, log

from windows.main_menu import MainMenu

from PySide6.QtCore import Qt, QSettings
from PySide6.QtGui import QFont, QFontDatabase, QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

if __name__ == "__main__":

    try:

        # application setup
        app = QApplication(sys.argv)
        QApplication.setOrganizationName("Beyond Earth Studios")
        QApplication.setOrganizationDomain("https://github.com/Beyond-Earth-Game-Studio")
        QApplication.setApplicationName("VortV")

        # init qsettings
        settings = QSettings()

        # windows are never resized on start
        settings.setValue("resized", 0)

        # init and clear log
        logging_init(True)

        # font stuff
        primary_font = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(':/fonts/Xolonium-Regular.otf'))[0]
        QApplication.setFont(QFont(primary_font, 10))

        # splash screen (must be after font stuff)
        splash = QPixmap(":/icons/logo.jpg")
        splash_screen = QSplashScreen(splash)
        splash_screen.show()
        splash_screen.showMessage("Loading Assets", alignment=Qt.AlignBottom, color=Qt.white)
        sleep(2)
        splash_screen.showMessage("Loading Game", alignment=Qt.AlignBottom, color=Qt.white)
        sleep(2)

        # fusion is a built-in Qt theme
        app.setStyle('Fusion')
        stylize(app)  # using css from style.py, works across modules :)

        # prepare for run
        menu = MainMenu()
        splash_screen.finish(menu)
        menu.show()

        # run
        app.exec()

    except Exception as error:
        logging_exit(error, True)
        print(f'\n[Error] - [{datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}]: {error}')

    finally:
        logging_exit('shutdown', False)
        print(f'\nShutting down: {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}')
        sys.exit()
