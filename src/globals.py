import resources
from PySide6.QtCore import QSettings
from PySide6.QtGui import QFontDatabase

def fonts() -> tuple[str, str]:
    """
    Returns a tuple of two font strings
    """
    primary = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(':/fonts/Xolonium-Regular.otf'))[0]
    title = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(':/fonts/DiaryOfAn8BitMage.ttf'))[0]

    return primary, title

def scale() -> tuple[int, int]:
    """
    Checks if scale has been set on first run
    """
    settings = QSettings("Beyond Earth Studios", "VortV")

    try:
        resolution = settings.value("Render Scale")

    except:
        resolution = None

    if resolution is None or (None, None):
        settings.setValue("scale", (200, 200))
        resolution = settings.value("Render Scale")

    return resolution

def index_check() -> tuple[int, int]:
    """
    Checks settings QComboBox indexes
    """
    settings = QSettings("Beyond Earth Studios", "VortV")

    try:
        index = (int(settings.value("Size Index")), int(settings.value("Scale Index")))
        print(index)
        print(type(index))

    except:
        index = None

    if index is None: #or tuple[None, None]: # or (int, None) or (None, int):
        settings.setValue("Size Index", 0)
        settings.setValue("Scale Index", 0)
        index = (settings.value("Size Index"), settings.value("Scale Index"))

    print(index)
    return index