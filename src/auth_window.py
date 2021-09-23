import sys

from gui.ui_auth_window import UiAuthWindow
from qt_core import *

class AuthWindow(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self)
        self.ui = UiAuthWindow()
        self.ui.setupUi(self)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.frame.mouseMoveEvent = self.moveWindow

        self.show()

    def moveWindow(self, event):
        self.windowHandle().startSystemMove()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()

    sys.exit(app.exec())