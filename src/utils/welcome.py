from datetime import datetime

def welcomemsg():
    """
    Displays welcome message and time / date
    """

    with open("data/welcomemsg.txt", "r") as file:
        msg = f'{file.readline()} \n'

    msg += datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # dd/mm/YY H:M:S

    return msg