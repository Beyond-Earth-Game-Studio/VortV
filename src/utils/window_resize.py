from utils.logger import log
from utils.window_check import check
from PySide6.QtCore import QSettings

settings = QSettings("Beyond Earth Studios", "VortV")

def initial_resize(target_window, target_window_name) -> None:
    forced = check(False)
    if forced:
        target_window.setGeometry(settings.value("Window_Geometry"))
        if settings.value("Target_Size") is not None:
            log(f'Forcing {target_window_name} to target size: {settings.value("Target_Size")}', False)
        else:
            log("Uh oh, me no found target size", False)

    else:
        target_window.showMaximized()
        log(f'Maximizing {target_window_name} menu', False)

def runtime_resize(target_window) -> None:
    """
    Resize a window during runtime after user has changed it in settings
    """
    try:
        resized = bool(int(settings.value("Resized_During_Runtime")))
    except:
        resized = None

    if resized == None:
        settings.setValue("resized", 0)
        resized = bool(int(settings.value("Resized_During_Runtime")))

    if resized:
        is_now_forced = bool(int(settings.value("Is_Forced_Size")))

        log("Size changed since last open - Trying to resize", True)
        log(f'Resizing window: {target_window}', True)

        if is_now_forced:
            log(f'Attempting resize to: {settings.value("Target_Size")}', True)
            log(f'Target geometry: {settings.value("Window_Geometry")}', False)

            target_window.setGeometry(settings.value("Window_Geometry"))

            log(f'Geometry after resize: {target_window.geometry()}', False)

            if target_window.geometry() != settings.value("Window_Geometry"):
                log("Resize Failed", True)
            else:
                log("Resize Successful", True)

            ''' Other method...
                if settings.value("Target_Size") == "700x450":
                    target_window.resize(700, 450)
            '''

        else:
            log("Attempting to autoscale, maximizing", True)

            target_window.showMaximized()

            if target_window.isMaximized():
                log("Autoscale Successful", True)
            else:
                log("Autoscale Failed", True)
