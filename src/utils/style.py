def stylize(target):

    style = (

        """
        QWidget#MainMenu, #SettingsWindow {
        background-color: QLinearGradient(x1: 1, y1: 5, x2: 0, y2: 0, stop: 0 cyan, stop: 1 #1f2324)}
        """

        """
        QPushButton#UIButton{
        padding: 10px;
        border-radius: 15px}
        """

        """
        QPushButton#MenuButton{
        font-size: 20px;}
        """

        """
        QPushButton {
        background-color: #4cc2d4;
        border-radius: 25px;
        border: 1px solid white}
        """

        """
        QPushButton:hover {
        background-color: #4299a6;
        border-radius: 25px;}
        """

        """
        QMessageBox QPushButton {
        padding: 5px;
        background-color: #4cc2d4;
        border-radius: 14px;
        min-width:45px;}
        """

        """
        QMessageBox QPushButton:hover {
        background-color: #4299a6;
        border-radius: 14px;}
        """

        """
        QMessageBox {
        background-color: QLinearGradient(x1: 1, y1: 5, x2: 0, y2: 0, stop: 0 cyan, stop: 1 #1f2324);
        border-radius: 25px;
        font-size: 15px;
        }
        """
    )

    target.setStyleSheet(style)

    return None
