from qt_core import *

from gui.widgets.background_label import BackgroundLabel
from gui.widgets.push_button import PushButton
from gui.widgets.sys_buttons import SysButtons

from controllers.theme_manager import ThemeManager, Colors

from gui.ui_pages.ui_pages import UiApplicationPages

from utils import norm_resource_path

class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        parent.resize(960, 540)
        parent.setMinimumSize(960, 540)

        self.ThemeManager = ThemeManager()

        self.central_frame = QFrame()

        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left Menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet(f"background-color: \
            {self.ThemeManager.getColor(Colors.background_light)};")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        self.show_menu_button = PushButton(
            text = "Menu",
            text_color = f"{self.ThemeManager.getColor(Colors.text_light)}",
            icon_name = "menu.svg",
            btn_color = self.ThemeManager.getColor(Colors.background_light),
            btn_hover = self.ThemeManager.getColor(Colors.button_hover),
            btn_pressed = self.ThemeManager.getColor(Colors.button_press),
            btn_is_pressed = self.ThemeManager.getColor(Colors.background)
        )
        self.home_button = PushButton(
            text = "Home page",
            text_color = f"{self.ThemeManager.getColor(Colors.text_light)}",
            icon_name = "home.svg",
            btn_color = self.ThemeManager.getColor(Colors.background_light),
            btn_hover = self.ThemeManager.getColor(Colors.button_hover),
            btn_pressed = self.ThemeManager.getColor(Colors.button_press),
            btn_is_pressed = self.ThemeManager.getColor(Colors.background),
            is_activate = True
        )
        self.btn_2 = PushButton(
            text = "Notifications",
            text_color = f"{self.ThemeManager.getColor(Colors.text_light)}",
            icon_name = "bell.svg",
            btn_color = self.ThemeManager.getColor(Colors.background_light),
            btn_hover = self.ThemeManager.getColor(Colors.button_hover),
            btn_pressed = self.ThemeManager.getColor(Colors.button_press),
            btn_is_pressed = self.ThemeManager.getColor(Colors.background)
        )

        self.left_menu_top_layout.addWidget(self.show_menu_button)
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

        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        self.settings_button = PushButton(
            text = "Settings",
            icon_name = "settings.svg",
            btn_color = self.ThemeManager.getColor(Colors.background_light),
            btn_hover = self.ThemeManager.getColor(Colors.button_hover),
            btn_pressed = self.ThemeManager.getColor(Colors.background),
            btn_is_pressed = self.ThemeManager.getColor(Colors.background)
        )

        self.left_menu_bottom_layout.addWidget(self.settings_button)

        self.left_menu_label_verion = BackgroundLabel(
            text="v1.0.0",
            maximum_width=300,
            alignment=Qt.AlignCenter,
        )

        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_verion)


        self.content = QFrame()
        self.content.setStyleSheet(f'background-color: \
            {self.ThemeManager.getColor(Colors.background)};'
        )

        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.top_bar = QWidget()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet(f" \
            color: {self.ThemeManager.getColor(Colors.text)}; \
            background-color: \
                {self.ThemeManager.getColor(Colors.background_dark)}; \
        ")

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
        self.bottom_bar.setStyleSheet(f" \
            color: {self.ThemeManager.getColor(Colors.text)}; \
            background-color: \
                {self.ThemeManager.getColor(Colors.background_dark)}; \
        ")

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
                image: url("{norm_resource_path("resources/images/size_grip.png")}");
                width: 16px;
                height: 16px;
            }}
        """)

        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)
        self.bottom_bar_layout.addWidget(self.bottom_right_size_grip, 0)


        self.pages = QStackedWidget()
        self.pages.setStyleSheet(f"font-size: 12pt; color: \
            {self.ThemeManager.getColor(Colors.text_light)};")
        self.ui_pages = UiApplicationPages()
        self.ui_pages.setupUi(self.pages)


        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        parent.setCentralWidget(self.central_frame)