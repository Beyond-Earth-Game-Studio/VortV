def center(self) -> None:
    """
    function to center a window - seems like it acts differently on linux
    """
    frame = self.frameGeometry()
    screen = self.window().windowHandle().screen()
    frame.moveCenter(screen.geometry().center())
    self.move(frame.topLeft())