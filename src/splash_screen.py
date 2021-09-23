
import sys
from qt_core import *

from gui.ui_splash_screen import UiSplashScreen

class SplashScreen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = UiSplashScreen()
        self.ui.setupUi(self)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.counter = 0
        self.timer.start(10)

        self.show()


    def progress(self):

        self.ui.progressBar.setValue(self.counter)
        if self.counter > 100:
            self.timer.stop()

            self.close()

        self.counter += 0.5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()

    sys.exit(app.exec())