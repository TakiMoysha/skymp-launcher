import sys

from qt_core import *
from settings import *

from gui.ui_main_window import UiMainWindow
from gui.widgets.push_button import PushButton
from gui.utils.dialog import getExistingDirectoryByFileDialog
from gui.widgets.notification_box import NotificationBox
from gui.utils.ui_utils import UIFunctions, WidgetsProvider

from controllers.path_validate import isPathToSkyrim

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(APPLICATION_NAME)
        self.settings = Settings()

        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.central_frame.setGraphicsEffect(self.shadow)

        WidgetsProvider.initStatusBar(self.ui.bottom_status_left)

        self.setupButtons()

        UIFunctions.removeDefaultTitleBar(self)
        self.setMouseTracking(True)

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
    def setupButtons(self):
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
        self.ui.ui_pages.ui_page_settings.openSkyrimFolder.clicked.connect(
            lambda: self.setupSkyrimDir()
        )



# Functions
    def setMouseTracking(self, flag):
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
        size_trigger_box_resize_mod = 3

        if y <= size_trigger_box_resize_mod:
            edge |= Qt.TopEdge
        if x <= size_trigger_box_resize_mod:
            edge |= Qt.LeftEdge
        if x >= self.width() - size_trigger_box_resize_mod:
            edge |= Qt.RightEdge
        if y >= self.height() - size_trigger_box_resize_mod:
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
                SettingsAttribute.skyrim_path,
                path_to_skyrim
            )
        else:
            NotificationBox(
                title = "Launcher says:",
                text = "Its not valid path to Skyrim"
            )


    def loadSettings(self):
        self.ui.ui_pages.ui_page_settings.pathToSkyrimFolder.setText(
            self.settings.getValue(SettingsAttribute.skyrim_path, "")
        )
        self.ui.ui_pages.ui_page_home.ui_servers_list.combo_box_master_servers.addItems(
            self.settings.getValue(SettingsAttribute.master_servers)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    sys.exit(app.exec())