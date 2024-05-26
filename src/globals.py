import resources
from PySide6.QtGui import QFontDatabase

def fonts() -> tuple[str, str]:    
    primary = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(':/fonts/Xolonium-Regular.otf'))[0]
    title = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(':/fonts/DiaryOfAn8BitMage.ttf'))[0]

    return primary, title