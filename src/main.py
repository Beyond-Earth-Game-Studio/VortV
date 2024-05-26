import sys
import resources

from datetime import datetime

from globals import fonts

from utils.style import stylize
from utils.logger import logging_init, logging_exit, log

from window_manager import WindowManager

from PySide6.QtGui import QFont
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QApplication

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
        primary_font = fonts()[0]
        QApplication.setFont(QFont(primary_font, 10))

        # fusion is a built-in Qt theme
        app.setStyle('Fusion')
        stylize(app)  # using css from style.py, works across modules :)

        # init window manger
        window_manager = WindowManager()
        window_manager.run_splash()
        window_manager.open_menu()

        # run
        app.exec()

    except Exception as error:
        logging_exit(error, True)
        print(f'\n[Error] - [{datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}]: {error}')

    finally:
        logging_exit('shutdown', False)
        print(f'\nShutting down: {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}')
        sys.exit()
