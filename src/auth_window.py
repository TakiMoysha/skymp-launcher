import sys
from gui.utils.dialog import showWarningMessage
from qt_core import *
from settings import Settings, SettingsAttribute

from controllers.authorization import login_user

from gui.ui_auth_window import UiAuthWindow

class AuthWindow(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self)
        self.ui = UiAuthWindow()
        self.ui.setupUi(self)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.frame.mouseMoveEvent = self.moveWindow

        self.settings = Settings()

        self.setupButtons()


    def moveWindow(self, event):
        self.windowHandle().startSystemMove()


    def setupButtons(self):
        self.ui.login_button.clicked.connect(
            lambda: self.loginClick()
        )
        self.ui.registration_button.clicked.connect(
            lambda: self.registrationClick()
        )
        self.ui.forgot_password_button.clicked.connect(
            lambda: self.forgotPasswordClick()
        )


    def loginClick(self):
        master_server = self.ui.master_server_combo_box.currentText()
        email = self.ui.email_line_edit.text()
        password = self.ui.password_line_edit.text()

        if not email:
            self.ui.setUncorrectEmailStyle()
        elif email:
            self.ui.setCorrectEmailStyle()
        if not password:
            self.ui.setUncorrectPasswordStyle()
        elif password:
            self.ui.setCorrectPasswordStyle()

        if not email or not password:
            return

        result_dict = login_user(master_server, email, password)
        if not result_dict: showWarningMessage(parent=self, text="Login failed")


    def registrationClick(self):
        # Change ui to ui_registration
        pass


    def forgotPasswordClick(self):
        # Change ui to ui_forgot_password
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()

    sys.exit(app.exec())