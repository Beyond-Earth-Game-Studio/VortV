from utils.logger import log
from PySide6.QtCore import QSettings

settings = QSettings("Beyond Earth Studios", "VortV")

def check() -> bool:
    """
    Checks if window size is forced or autoscaled
    """
    try:
        forced = bool(int(settings.value("forced size")))
    except:
        forced = None

    if forced is None:
        settings.setValue("forced size", 0)

    else:
        log(f'Is forced size: {forced}', True)

        if settings.value("target size") is not None:
            log(f'Target Size: {settings.value("target size")}', False)
        else:
            log('Target Size: Unknown, please change window size once', False)

        return forced