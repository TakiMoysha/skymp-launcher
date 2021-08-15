from qt_core import *

class NotificationBox(QMessageBox):
    def __init__(
        self,
        title = "",
        text = "",
    ):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.exec()

    def retranslateUi(self):
        pass