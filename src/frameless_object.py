from qt_core import *

class FramelessObject(QObject):
    Margins = 5
    TitleHeight = 36
    Widgets = set()

    @classmethod
    def setMargins(cls, margins):
        cls.Margins = margins


    @classmethod
    def setTitleHeight(cls, height):
        cls.TitleHeight = height

    @classmethod
    def addWidget(cls, widget):
        cls.Widgets.add(widget)

    @classmethod
    def removeWidget(cls, widget):
        if widget in cls.Widgets:
            cls.Widgets.remove(widget)


    def _getEdges(self, pos: QPoint, width: int, height: int):
        """"""
        edge = 0
        x, y = pos.x(), pos.y()
        if y <= self.Margins:
            edge |= Qt.TopEdge
        if x <= self.Margins:
            edge |= Qt.LeftEdge
        if x >= width - self.Margins:
            edge |= Qt.RightEdge
        if y >= height - self.Margins:
            edge |= Qt.BottomEdge

        return edge


    def _getCursor(self, edges: int) -> Qt.CursorShape:
        if edges == Qt.LeftEdge | Qt.TopEdge or edges == Qt.RightEdge | Qt.BottomEdge:
            return Qt.SizeFDiagCursor
        elif edges == Qt.RightEdge | Qt.TopEdge or edges == Qt.LeftEdge | Qt.BottomEdge:
            return Qt.SizeBDiagCursor
        elif edges == Qt.LeftEdge or edges == Qt.RightEdge:
            return Qt.SizeHorCursor
        elif edges == Qt.TopEdge or edges == Qt.BottomEdge:
            return Qt.SizeVerCursor

        return Qt.ArrowCursor


    def isTitlebar(self, pos: QPoint) -> bool:
        return pos.y() <= self.TitleHeight


    def moveOrResize(self, window, pos, width, height):
        edges = self._getEdges(pos, width, height)
        if edges:
            if window.windowState() == Qt.WindowNoState:
                window.startSystemResize(edges)
        else:
            if self.isTitlebar(pos):
                window.startSystemMove()


    def eventFilter(self, obj, event):
        if obj.isWindowType():
            if event.type() == QEvent.MouseMove and obj.windowState() == Qt.WindowNoState:
                obj.setCursor(self._getCursor(self._getEdges(event.pos(), obj.width(), obj.height())))
            elif event.type() == QEvent.TouchUpdate:
                self.moveOrResize(obj, event.pos(), obj.width(), obj.height())
        elif obj in self.Widgets and isinstance(event, QMouseEvent) and event.button() == Qt.LeftButton:
            if event.type() == QEvent.MouseButtonDblClick:
                if self.isTitlebar(event.pos()):
                    if obj.windowState() == Qt.WindowFullScreen:
                        pass
                    elif obj.windowState() == Qt.WindowMaximized:
                        obj.showNormal()
                    else:
                        obj.showMaximized()
            elif event.type() == QEvent.MouseButtonPress:
                self.moveOrResize(obj.windowHandle(), event.pos(), obj.width(), obj.height())

        return False

