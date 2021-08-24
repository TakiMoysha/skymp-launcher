
import sys

from qt_core import *
from settings import *

from gui.ui_main_window import *
from gui.utils.ui_functions import *
from gui.utils.dialog import getExistingDirectoryByFileDialog
from gui.widgets.notification_box import NotificationBox
from gui.utils.ui_functions import UIFunctions

from controllers.path_validate import isPathToSkyrim

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(APPLICATION_NAME)
        self.settings = Settings()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.ui.show_menu_button.clicked.connect(self.showMenu)

        self.ui.home_button.clicked.connect(self.showPageHome)
        self.ui.btn_2.clicked.connect(self.showPage2)
        self.ui.settings_button.clicked.connect(self.showPageSettings)

        self.ui.ui_title_bar.ui_sys_buttons.button_minimize.clicked.connect(
            lambda: self.setWindowState(Qt.WindowMinimized)
        )
        self.ui.ui_title_bar.ui_sys_buttons.button_maximize.clicked.connect(
            lambda: UIFunctions.maximizeWindow(
                self,
                self.ui.ui_title_bar.ui_sys_buttons.button_maximize
            )
        )
        self.ui.ui_title_bar.ui_sys_buttons.button_exit.clicked.connect(
            lambda: self.close()
        )

        def mouseMoveEvent(event):
            if self.windowState() == Qt.WindowMaximized:
                self.setWindowState(Qt.WindowNoState)
                self.move(event.pos())
            if (event.buttons() == Qt.LeftButton):
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = mouseMoveEvent

        UIFunctions.removeDefaultTitleBar(self)

        self.settingsPageInitButtons()

        self.loadSettings()
        self.show()

# Events
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def changeEvent(self, event: QEvent):
        super().changeEvent(event)
        visible = self.isMaximized()
        if visible:
            self.layout().setContentsMargins(0, 0, 0, 0)
        else:
            m = self.layout().setContentsMargins(5, 5, 5, 5)

# Functions
    def showMenu(self):
        menu_width = self.ui.left_menu.width()

        width = 50
        if menu_width == 50:
            width = 140

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(150)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start()


    def showPageHome(self):
        self.resetSelection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_home)
        self.ui.home_button.setActive(True)


    def showPage2(self):
        self.resetSelection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.setActive(True)


    def showPageSettings(self):
        self.resetSelection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_settings)
        self.ui.settings_button.setActive(True)

    def resetSelection(self):
        for btn in self.ui.left_menu.findChildren(PushButton):
            btn.setActive(False)


    def settingsPageInitButtons(self):
        self.ui.ui_pages.ui_page_settings.openSkyrimFolder.clicked.connect(
            lambda: self.setupSkyrimDir()
        )


    def setupSkyrimDir(self):
        path_to_skyrim = getExistingDirectoryByFileDialog(
            self.ui.ui_pages.ui_page_settings.pathToSkyrimFolder.text()
        )
        if (path_to_skyrim == ""):
            pass
        elif isPathToSkyrim(path_to_skyrim):
            self.ui.ui_pages.ui_page_settings.pathToSkyrimFolder.setText(
                path_to_skyrim
            )
            self.settings.saveValue(
                Settings.SettingsType.skyrim_path,
                path_to_skyrim
            )
        else:
            NotificationBox(
                title = "Launcher says:",
                text = "Its not valid path to Skyrim"
            )

    def loadSettings(self):
        self.ui.ui_pages.ui_page_settings.pathToSkyrimFolder.setText(
            self.settings.getValue(Settings.SettingsType.skyrim_path, "")
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())