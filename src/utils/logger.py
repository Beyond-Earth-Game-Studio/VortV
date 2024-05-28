from datetime import datetime
from PySide6.QtCore import QSettings

settings = QSettings("Beyond Earth Studios", "VortV")

try:
    log_level = settings.value("Log_Level")

except:
    log_level = None

if log_level is None:
    settings.setValue("Log_Level", "Verbose")
    log_level = settings.value("Log_Level")

def logging_init(clear: bool) -> None:
    """
    Initialize logging, will clear logs on game start if clear = True
    """
    mode = 'a'
    if clear:
        mode = 'w'

    with open("logs/game_log.txt", mode) as logfile:
        logfile.write(f'[Start] - Program start: {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}\n')
        logfile.write(f'[Log Level]: {log_level}\n\n')

def logging_exit(msg: str, error: bool) -> None:

    with open("logs/game_log.txt", "a") as logfile:

        if error:
            logfile.write(f'\n[Error] - [{datetime.now().strftime("%H:%M:%S")}]: {msg}\n')

        else:
            logfile.write(f'\n[Exit] - Shutting down: {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}\n\n')

def log(msg: str, warn: bool) -> None:
    """
    Log level aware logging function
    """
    with open("logs/game_log.txt", "a") as logfile:

        if log_level == "Verbose" and not warn:
            logfile.write(f'[Verbose] - [{datetime.now().strftime("%H:%M:%S")}]: {msg}\n')

        if log_level == "Verbose" and warn:
            logfile.write(f'[Warning] - [{datetime.now().strftime("%H:%M:%S")}]: {msg}\n')

        if log_level == "Warn" and warn:
            logfile.write(f'[Warning] - [{datetime.now().strftime("%H:%M:%S")}]: {msg}\n')

def change_log(selected_log_level: str, box_is_checked: bool) -> str:
    """
    Function to change log level
    """
    if selected_log_level == "Verbose" and box_is_checked:

        if selected_log_level != settings.value("Log_Level"):
            log("Setting log level to 'Verbose' - will take effect on next restart", True)

        settings.setValue("Log_Level", "Verbose")

    if selected_log_level == "Warn" and box_is_checked:

        if selected_log_level != settings.value("Log_Level"):
            log("Setting log level to 'Warn' - will take effect on next restart", True)

        settings.setValue("Log_Level", "Warn")

    if selected_log_level == "Error" and box_is_checked:

        if selected_log_level != settings.value("Log_Level"):
            log("Setting log level to 'Error' - will take effect on next restart", True)

        settings.setValue("Log_Level", "Error")

    return settings.value("Log_Level")