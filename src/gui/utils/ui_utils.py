from qt_core import *
from main_window import *

class UIFunctions():
    def removeDefaultTitleBar(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)


    def maximized(window: QMainWindow, called_button: QPushButton):
        called_button.setToolTip("Restore")
        window.showMaximized()


    def restore(window: QMainWindow, called_button: QPushButton):
        called_button.setToolTip("Maximize")
        window.showNormal()


    def toggleMaximized(self: QMainWindow, called_button: QPushButton):
        if (self.windowState() == Qt.WindowNoState):
            UIFunctions.maximized(window=self, called_button=called_button)
        else:
            UIFunctions.restore(window=self, called_button=called_button)


    def getCursor(edges):
        """which cursor icon to display"""
        if edges == Qt.LeftEdge | Qt.TopEdge or edges == Qt.RightEdge | Qt.BottomEdge:
            return Qt.SizeFDiagCursor
        elif edges == Qt.RightEdge | Qt.TopEdge or edges == Qt.LeftEdge | Qt.BottomEdge:
            return Qt.SizeBDiagCursor
        elif edges == Qt.LeftEdge or edges == Qt.RightEdge:
            return Qt.SizeHorCursor
        elif edges == Qt.TopEdge or edges == Qt.BottomEdge:
            return Qt.SizeVerCursor

        return Qt.ArrowCursor


    def _getEdges(pos, width, height):
        """what an edge this is"""
        edge = 0
        x, y = pos.x(), pos.y()
        Margins = 5

        if y <= Margins:
            print(y)
            edge |= Qt.TopEdge
        if x <= Margins:
            print(x)
            edge |= Qt.LeftEdge
        if x >= width - Margins:
            print(x)
            edge |= Qt.RightEdge
        if y >= height - Margins:
            print(y)
            edge |= Qt.BottomEdge

        return edge


class WidgetsProvider:
    """Stores links to widgets used from different locations in the application"""
    linkToStatusBar = None

    @classmethod
    def initStatusBar(cls, status_bar: QStatusBar):
        cls.linkToStatusBar = status_bar

    @classmethod
    def setStatus(cls, text):
        cls.linkToStatusBar.showMessage(text)