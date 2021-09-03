
import sys

from qt_core import *
from settings import *

from gui.ui_main_window import UI_MainWindow
from gui.utils.dialog import getExistingDirectoryByFileDialog
from gui.widgets.notification_box import NotificationBox
from gui.utils.ui_utils import UIFunctions, StaticWidget

from controllers.path_validate import isPathToSkyrim

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(APPLICATION_NAME)
        self.settings = Settings()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        StaticWidget.initStatusBar(self.ui.bottom_status_left)

        self.handle_buttons()

        UIFunctions.removeDefaultTitleBar(self)
        self._setMouseTracking(True)

        self.settingsPageInitButtons()

        self.loadSettings()
        self.show()


# Override
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPosition().toPoint()


    def event(self, event: QEvent):
        super().event(event)

        def isMoveWindow():
            isTypeMove = event.type() == QEvent.MouseMove
            isWindowNoState = self.windowState() == Qt.WindowNoState
            return isTypeMove and isWindowNoState

        if isMoveWindow():
            self.setCursor(
                UIFunctions.getCursor(
                    self.getEdges(event.position().toPoint())
                )
            )
        elif event.type() == QEvent.TouchUpdate:
            self.moveOrResize(self, event.position().toPoint())
        elif (isinstance(event, QMouseEvent) and event.button() == Qt.LeftButton):
            if event.type() == QEvent.MouseButtonDblClick:
                if event.position().toPoint().y() <= 36:
                    if self.windowState() == Qt.WindowFullScreen:
                        pass
                    elif self.windowState() == Qt.WindowMaximized:
                        self.showNormal()
                    else:
                        self.showMaximized()
            elif event.type() == QEvent.MouseButtonPress:
                self.moveOrResize(
                    self.windowHandle(),
                    event.position().toPoint(),
                )

        return False

#
    def handle_buttons(self):
        self.ui.ui_title_bar.ui_sys_buttons.button_minimize.clicked.connect(
            lambda: self.setWindowState(Qt.WindowMinimized)
        )
        self.ui.ui_title_bar.ui_sys_buttons.button_maximize.clicked.connect(
            lambda: UIFunctions.toggleMaximized(
                self,
                self.ui.ui_title_bar.ui_sys_buttons.button_maximize
            )
        )
        self.ui.ui_title_bar.ui_sys_buttons.button_exit.clicked.connect(
            lambda: self.close()
        )

        self.ui.show_menu_button.clicked.connect(self.showMenu)

        self.ui.home_button.clicked.connect(self.showPageHome)
        self.ui.btn_2.clicked.connect(self.showPage2)
        self.ui.settings_button.clicked.connect(self.showPageSettings)


# Functions
    def _setMouseTracking(self, flag):
        def recursive_set(parent):
            for child in parent.findChildren(QObject):
                try:
                    child.setMouseTracking(flag)
                except:
                    pass
                recursive_set(child)
        QWidget.setMouseTracking(self, flag)
        recursive_set(self)


    def getEdges(self, pos):
        """what an edge this is"""
        edge = 0
        x, y = pos.x(), pos.y()
        Margins = 3

        if y <= Margins:
            edge |= Qt.TopEdge
        if x <= Margins:
            edge |= Qt.LeftEdge
        if x >= self.width() - Margins:
            edge |= Qt.RightEdge
        if y >= self.height() - Margins:
            edge |= Qt.BottomEdge

        return edge


    def moveOrResize(self, window, pos):
        edges = self.getEdges(pos)
        if edges:
            if window.windowState() == Qt.WindowNoState:
                window.startSystemResize(edges)
        else:
            if pos.y() <= self.ui.title_bar.height():
                window.startSystemMove()


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
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    sys.exit(app.exec())