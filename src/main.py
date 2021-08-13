
import sys
import os

from qt_core import *

from gui.pages.ui_main_window import *
from gui.pages.utils.ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SkyMP")

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.ui.toggle_button.clicked.connect(self.toggleButton)

        self.ui.home_button.clicked.connect(self.showPageHome)
        self.ui.btn_2.clicked.connect(self.showPage2)
        self.ui.settings_button.clicked.connect(self.showPageSettings)

        self.ui.ui_top_label_right.button_minimize.clicked.connect(
            lambda: self.showMinimized()
        )
        self.ui.ui_top_label_right.button_maximize.clicked.connect(
            lambda: UIFunctions.maximize_window(self)
        )
        self.ui.ui_top_label_right.button_exit.clicked.connect(
            lambda: self.close()
        )

        UIFunctions.remove_default_title_bar(self)

        self.show()
        print("Create")


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


    def toggleButton(self):
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())