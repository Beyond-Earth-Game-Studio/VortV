from utils.logger import log
from PySide6.QtCore import QSettings

settings = QSettings("Beyond Earth Studios", "VortV")

def check(init: bool) -> bool:
    """
    Checks if window size is forced or autoscaled
    """
    try:
        forced = bool(int(settings.value("Is_Forced_Size")))
    except:
        forced = None

    if forced is None:
        settings.setValue("Is_Forced_Size", 0)
        forced = bool(int(settings.value("Is_Forced_Size")))

    if init:
        log(f'Is forced size: {forced}', True)

        if settings.value("Target_Size") is not None:
            log(f'Target Size: {settings.value("Target_Size")}', False)

        else:
            log('Target Size: Unknown - Please change window size once', False)

    return forced