from qt_core import *

from controllers.theme_manager import ThemeManager, Colors

class UiSplashScreen(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(501, 331)

        tm = ThemeManager()
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 481, 311))
        self.frame.setStyleSheet(f"""QFrame {{
            border-radius: 10px;
        	background-color: {tm.getColor(Colors.background)};
        }}""")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 461, 60))
        self.label.setStyleSheet(f"""QLabel {{
            color: {tm.getColor(Colors.text)};
        }}""")
        self.label.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 230, 441, 23))
        self.progressBar.setStyleSheet(f"""QProgressBar{{
            background-color: {tm.getColor(Colors.background_light)};
            color: {tm.getColor(Colors.text)};
            border-style: none;
            border-radius: 8px;
            }}
        QProgressBar::chunk {{
            border-radius: 8px;
            background-color: qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.522727, stop:0 {tm.getColor(Colors.button_hover)}, stop:1 {tm.getColor(Colors.button)});
        }}""")

        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 260, 461, 41))
        self.label_2.setStyleSheet(f"""QLabel {{
            color: {tm.getColor(Colors.text)};
        }}""")

        self.label_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">Skyrim Multiplayer </span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Loading...</p></body></html>", None))
    # retranslateUi

