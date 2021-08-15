from qt_core import *

from gui.pages.ui_pages import Ui_application_pages

from gui.pages.widgets.push_button import PushButton
from gui.pages.widgets.sys_buttons import SysButtons
from gui.pages.widgets.title_bar_button import TitleBarButton
from utils import resource_path, norm_resource_path

class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        parent.resize(960, 540)
        parent.setMinimumSize(960, 540)

        self.central_frame = QFrame()

        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left Menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: rgb(54, 73, 125)")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet(
            "#left_menu_top_frame { background-color: red; }"
        )

        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        self.toggle_button = PushButton(
            text = "Menu",
            icon_name = "menu.svg"
        )
        self.home_button = PushButton(
            text = "Home page",
            icon_name = "home.svg",
            is_activate = True
        )
        self.btn_2 = PushButton(
            text = "Notifications",
            icon_name = "bell.svg"
        )

        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.home_button)
        self.left_menu_top_layout.addWidget(self.btn_2)

        self.left_menu_spacer = QSpacerItem(
            20,
            20,
            QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )

        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet(
            "# left_menu_bottom_frame { background-color: red; }"
        )

        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        self.settings_button = PushButton(
            text = "Settings",
            icon_name = "settings.svg"
        )

        self.left_menu_bottom_layout.addWidget(self.settings_button)

        self.left_menu_label_verion = QLabel("v1.0.0")
        self.left_menu_label_verion.setAlignment(Qt.AlignCenter)
        self.left_menu_label_verion.setMinimumHeight(25)
        self.left_menu_label_verion.setMaximumHeight(25)
        self.left_menu_label_verion.setStyleSheet("color: rgb(195, 204, 223)")

        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_verion)



        self.content = QFrame()
        self.content.setStyleSheet("background-color: rgb(33, 45, 80)")

        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.top_bar = QWidget()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("color: rgb(195, 204, 223); background-color: rgb(30, 48, 98)")

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 4, 0)

        self.top_label_left = QLabel("SkyMP Launcher")

        self.top_spacer = QSpacerItem(
            100,
            20,
            QSizePolicy.Maximum,
            QSizePolicy.Minimum
        )

        self.top_label_right = QHBoxLayout(self.top_bar)
        self.ui_top_label_right = SysButtons()
        self.ui_top_label_right.setupUi(self.top_label_right)

        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addLayout(self.top_label_right)

        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(25)
        self.bottom_bar.setMaximumHeight(25)
        self.bottom_bar.setStyleSheet("color: rgb(195, 204, 223); background-color: rgb(30, 48, 98)")

        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(8, 0, 8, 0)

        self.bottom_label_left = QLabel("Status text")

        self.bottom_spacer = QSpacerItem(
            20,
            20,
            QSizePolicy.Expanding,
            QSizePolicy.Minimum
        )

        self.bottom_label_right = QLabel("| RED HOUSE")
        self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        self.bottom_right_size_grip = QSizeGrip(self.bottom_bar)
        self.bottom_right_size_grip.setStyleSheet(f"""
            QSizeGrip {{
                image: url("{norm_resource_path("assets/images/size_grip.png")}");
                width: 16px;
                height: 16px;
            }}
        """)

        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)
        self.bottom_bar_layout.addWidget(self.bottom_right_size_grip, 0)


        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)


        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)



        parent.setCentralWidget(self.central_frame)