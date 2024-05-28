import resources
from utils.logger import log
from PySide6.QtCore import QSettings
from PySide6.QtGui import QFontDatabase

settings = QSettings("Beyond Earth Studios", "VortV")

def fonts() -> tuple[str, str]:
    """
    Returns a tuple of two font strings
    """
    primary = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(':/fonts/Xolonium-Regular.otf'))[0]
    title = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(':/fonts/DiaryOfAn8BitMage.ttf'))[0]

    return primary, title

def scale(init: bool) -> tuple[int, int]:
    """
    Checks render scale
    """
    try:
        resolution = int(settings.value("Render_Scale"))

    except:
        resolution = None

    if resolution is None:
        settings.setValue("Render_Scale", 200)
        resolution = int(settings.value("Render_Scale"))

    if init:
        log(f'Render scale: {resolution}', False)

    return resolution, resolution

def index_check() -> tuple[int, int]:
    """
    Checks settings QComboBox indexes
    """
    try:
        size_index = settings.value("Size_Index")

    except:
        size_index = None

    try:
        scale_index = settings.value("Scale_Index")

    except:
        scale_index = None

    # ... == (None, None) matches all tuples.... 
    if size_index is None:
        settings.setValue("Size_Index", 0)

    if scale_index is None:
        settings.setValue("Scale_Index", 0)

    return (int(settings.value("Size_Index")), int(settings.value("Scale_Index")))