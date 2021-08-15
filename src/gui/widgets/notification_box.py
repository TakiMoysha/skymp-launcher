from qt_core import *

class NotificationBox(QMessageBox):
    def __init__(
        self,
        icon = QMessageBox.Warning,
        title = "",
        text = "",
    ):
        super().__init__()
        self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(text)
        self.exec()

    def retranslateUi(self):
        pass

