from qt_core import *
from settings import *

from gui.widgets.button_with_icon import ButtonWithIcon
from gui.ui_auth_window_style import combo_box_style, line_edit_style

from controllers.theme_manager import ThemeManager, Colors
from utils import norm_resource_path

class UiAuthWindow():
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 473)
        Form.setStyleSheet(u"QFrame {\n"
"}")
        tm = ThemeManager()
        settings_app = Settings()

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 401, 451))
        self.frame.setStyleSheet(f"""QFrame {{
            outline: none;
            background-color: {tm.getColor(Colors.background)};
            border-radius: 8px;
        }}""")

        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 210, 381, 231))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.master_server_combo_box = QComboBox(self.verticalLayoutWidget)
        self.master_server_combo_box.setObjectName(u"master_server_combo_box")
        items = settings_app.getValue(SettingsAttribute.master_servers)
        self.master_server_combo_box.addItems(items)
        self.master_server_combo_box.setMinimumHeight(16)
        self.master_server_combo_box.setCursor(Qt.PointingHandCursor)
        image_arrow_path = norm_resource_path("./resources/icons/drop-down-arrow.svg")
        self.master_server_combo_box.setStyleSheet(combo_box_style.format(
            border_color=tm.getColor(Colors.button),
            background_color=tm.getColor(Colors.background_light),
            transparent=tm.getColor(Colors.transparent),
            text_color=tm.getColor(Colors.text),
            arrow_path=image_arrow_path
        ))

        self.verticalLayout_2.addWidget(self.master_server_combo_box)

        font = QFont()
        font.setPointSize(10)

        self.email_line_edit = QLineEdit(self.verticalLayoutWidget)
        self.email_line_edit.setObjectName(u"email_line_edit")
        self.email_line_edit.setFont(font)
        self.email_line_edit.setEchoMode(QLineEdit.Normal)
        self.email_line_edit.setPlaceholderText("Email")
        self.email_line_edit.setMinimumHeight(24)
        self.email_line_edit.setStyleSheet(line_edit_style.format(
            text_color=tm.getColor(Colors.text),
            background_color=tm.getColor(Colors.background_light),
            border_color=tm.getColor(Colors.button)
        ))

        self.verticalLayout_2.addWidget(self.email_line_edit)

        self.password_line_edit = QLineEdit(self.verticalLayoutWidget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setFont(font)
        self.password_line_edit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.password_line_edit.setPlaceholderText("Password")
        self.password_line_edit.setMinimumHeight(24)
        self.password_line_edit.setStyleSheet(line_edit_style.format(
            text_color=tm.getColor(Colors.text),
            background_color=tm.getColor(Colors.background_light),
            border_color=tm.getColor(Colors.button)
        ))

        self.verticalLayout_2.addWidget(self.password_line_edit)

        self.remember_me_box = QCheckBox(self.verticalLayoutWidget)
        self.remember_me_box.setObjectName(u"remember_me_box")
        self.remember_me_box.setStyleSheet(f"""
            QCheckBox {{
                color: {tm.getColor(Colors.text)}
            }}
        """)

        self.verticalLayout_2.addWidget(self.remember_me_box)

        self.login_button = ButtonWithIcon(
            text_color=tm.getColor(Colors.text),
            btn_color=tm.getColor(Colors.button),
            btn_hover=tm.getColor(Colors.button_hover),
            btn_press=tm.getColor(Colors.button_press)
        )
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout_2.addWidget(self.login_button)

        self.forgot_password_button = ButtonWithIcon(
            text_color=tm.getColor(Colors.text),
            btn_color=tm.getColor(Colors.button),
            btn_hover=tm.getColor(Colors.button_hover),
            btn_press=tm.getColor(Colors.button_press)
        )
        self.forgot_password_button.setObjectName(u"forgot_password_button")

        self.verticalLayout_2.addWidget(self.forgot_password_button)

        self.registration_button = ButtonWithIcon(
            text_color=tm.getColor(Colors.text),
            btn_color=tm.getColor(Colors.button),
            btn_hover=tm.getColor(Colors.button_hover),
            btn_press=tm.getColor(Colors.button_press)
        )
        self.registration_button.setObjectName(u"registration_button")

        self.verticalLayout_2.addWidget(self.registration_button)

        self.image = QLabel(self.frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(10, 60, 381, 141))
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setStyleSheet(f"""
            QLabel {{
                image: url({norm_resource_path("resources/icons/skyrim.svg")});
        }}""")

        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 381, 34))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        label_font = QFont()
        label_font.setPointSize(12)
        self.label.setFont(label_font)
        self.label.setStyleSheet(f"color:{tm.getColor(Colors.text_light)}")

        self.horizontalLayout.addWidget(self.label)

        self.exit_button = ButtonWithIcon(
            icon_name="close.svg",
            icon_type="icons",
            btn_color=tm.getColor(Colors.button),
            btn_hover=tm.getColor(Colors.button_hover),
            btn_press=tm.getColor(Colors.button_press)
        )
        self.horizontalLayout.addWidget(self.exit_button)
        self.exit_button.setObjectName(u"exit_button")

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setMinimumSize(QSize(24, 24))
        self.exit_button.setMaximumSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.exit_button)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.remember_me_box.setText(QCoreApplication.translate("Form", u"Remember me", None))
        self.login_button.setText(QCoreApplication.translate("Form", u"Login", None))
        self.forgot_password_button.setText(QCoreApplication.translate("Form", u"Forgot password", None))
        self.registration_button.setText(QCoreApplication.translate("Form", u"Registration", None))
        self.label.setText(QCoreApplication.translate("Form", u"Sign In", None))
    # retranslateUi


    def setCorrectEmailStyle(self):
        tm = ThemeManager()
        self.email_line_edit.setStyleSheet(line_edit_style.format(
            text_color=tm.getColor(Colors.text),
            background_color=tm.getColor(Colors.background_light),
            border_color=tm.getColor(Colors.button)

        ))

    def setUncorrectEmailStyle(self):
        tm = ThemeManager()
        self.email_line_edit.setStyleSheet(line_edit_style.format(
            text_color='red',
            background_color=tm.getColor(Colors.background_light),
            border_color=tm.getColor(Colors.button)
        ))

    def setCorrectPasswordStyle(self):
        tm = ThemeManager()
        self.password_line_edit.setStyleSheet(line_edit_style.format(
            text_color=tm.getColor(Colors.text),
            background_color=tm.getColor(Colors.background_light),
            border_color=tm.getColor(Colors.button)

        ))

    def setUncorrectPasswordStyle(self):
        tm = ThemeManager()
        self.password_line_edit.setStyleSheet(line_edit_style.format(
            text_color='red',
            background_color=tm.getColor(Colors.background_light),
            border_color=tm.getColor(Colors.button)
        ))