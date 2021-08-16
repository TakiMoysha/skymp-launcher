
import sys

from qt_core import *
from settings import *

from gui.ui_main_window import *
from gui.utils.ui_functions import *
from gui.utils.dialog import getExistingDirectoryByFileDialog
from gui.widgets.notification_box import NotificationBox

from adapter.path_validate import isPathToSkyrim


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

        self.ui.ui_top_label_right.button_minimize.clicked.connect(
            lambda: self.showMinimized()
        )
        self.ui.ui_top_label_right.button_maximize.clicked.connect(
            lambda: UIFunctions.maximizeWindow(self)
        )
        self.ui.ui_top_label_right.button_exit.clicked.connect(
            lambda: self.close()
        )

        def mouseMoveEvent(event):
            if (event.buttons() == Qt.LeftButton):
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.top_bar.mouseMoveEvent = mouseMoveEvent

        UIFunctions.removeDefaultTitleBar(self)

        self.settingsPageInitButtons()

        self.loadSettings()
        self.show()


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


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