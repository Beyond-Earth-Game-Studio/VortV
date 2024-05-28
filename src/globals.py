import resources
from utils.logger import log
from utils.window_check import check
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

def startup_checks(app) -> bool:
    # laptop is 2880 x 1880 -> 1440 x 900 (2x DPI Scaling)
    # pc is 3840 x 2160 -> 1920 x 1080 (also 2x Scaling)
    global screen_size 
    screen_size = app.primaryScreen().size().toTuple()

    log(f'Scaled screen size: {screen_size[0]}x{screen_size[1]}', True)

    try:
        forced = check(True)
    except:
        log('Window size check failed', True)
        return False
    try:
        render_scale = scale(True)
    except:
        log('Render scale check failed', True)
        return False

    return True

def screen_size_check() -> tuple[int, int]:
    return screen_size

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
        settings.setValue("Scale_Index", 2)

    return (int(settings.value("Size_Index")), int(settings.value("Scale_Index")))