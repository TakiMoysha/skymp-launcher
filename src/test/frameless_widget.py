import ctypes.wintypes
from ctypes.wintypes import POINT
import os
from PySide6.QtWidgets import QMainWindow

import win32api
import win32con
import win32gui

# try:
#     from PyQt5 import QtCore, QtGui, QtWidgets
#     from PyQt5.QtCore import QTimer, Qt, QEvent, QObject
#     from PyQt5.QtGui import QWindow, QPainter, QColor, QMouseEvent
#     from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
# except ImportError:
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QTimer, Qt, QEvent, QObject
from PySide2.QtGui import QWindow, QPainter, QColor, QMouseEvent
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox

class FramelessObject(QObject):
    Margins = 3  # 边缘边距
    TitleHeight = 36  # 标题栏高度
    Widgets = set()  # 无边框窗口集合

    @classmethod
    def set_margins(cls, margins):
        cls.Margins = margins

    @classmethod
    def set_title_height(cls, height):
        cls.TitleHeight = height

    @classmethod
    def add_widget(cls, widget):
        cls.Widgets.add(widget)

    @classmethod
    def del_widget(cls, widget):
        if widget in cls.Widgets:
            cls.Widgets.remove(widget)

    def _get_edges(self, pos, width, height):
        """根据坐标获取方向
        :param pos: QPoint
        :param width: int
        :param height: int
        :return: Qt.Edges
        """
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

    def _get_cursor(self, edges):
        """调整鼠标样式
        :param edges: int or None
        :return: Qt.CursorShape
        """
        if edges == Qt.LeftEdge | Qt.TopEdge or edges == Qt.RightEdge | Qt.BottomEdge:
            return Qt.SizeFDiagCursor
        elif edges == Qt.RightEdge | Qt.TopEdge or edges == Qt.LeftEdge | Qt.BottomEdge:
            return Qt.SizeBDiagCursor
        elif edges == Qt.LeftEdge or edges == Qt.RightEdge:
            return Qt.SizeHorCursor
        elif edges == Qt.TopEdge or edges == Qt.BottomEdge:
            return Qt.SizeVerCursor

        return Qt.ArrowCursor

    def is_titlebar(self, pos):
        """判断是否是标题栏
        :param pos: QPoint
        :return: bool
        """
        return pos.y() <= self.TitleHeight

    def moveOrResize(self, window, pos, width, height):
        edges = self._get_edges(pos, width, height)
        if edges:
            if window.windowState() == Qt.WindowNoState:
                window.startSystemResize(edges)
        else:
            if self.is_titlebar(pos):
                window.startSystemMove()

    def eventFilter(self, obj, event):
        if obj.isWindowType():
            # top window 处理光标样式
            if event.type() == QEvent.MouseMove and obj.windowState() == Qt.WindowNoState:
                obj.setCursor(self._get_cursor(self._get_edges(event.pos(), obj.width(), obj.height())))
            elif event.type() == QEvent.TouchUpdate:
                self.moveOrResize(obj, event.pos(), obj.width(), obj.height())
        elif obj in self.Widgets and isinstance(event, QMouseEvent) and event.button() == Qt.LeftButton:
            if event.type() == QEvent.MouseButtonDblClick:
                # 双击最大化还原
                if self.is_titlebar(event.pos()):
                    if obj.windowState() == Qt.WindowFullScreen:
                        pass
                    elif obj.windowState() == Qt.WindowMaximized:
                        obj.showNormal()
                    else:
                        obj.showMaximized()
            elif event.type() == QEvent.MouseButtonPress:
                self.moveOrResize(obj.windowHandle(), event.pos(), obj.width(), obj.height())

        return False



class Ui_FormFrameless(object):
    def setupUi(self, FormFrameless):
        FormFrameless.setObjectName("FormFrameless")
        FormFrameless.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormFrameless)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetTitleBar = QtWidgets.QWidget(FormFrameless)
        font = QtGui.QFont()
        font.setFamily("Symbola")
        self.widgetTitleBar.setFont(font)
        self.widgetTitleBar.setObjectName("widgetTitleBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetTitleBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonMinimum = QtWidgets.QPushButton(self.widgetTitleBar)
        self.buttonMinimum.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonMinimum.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("webdings")
        self.buttonMinimum.setFont(font)
        self.buttonMinimum.setObjectName("buttonMinimum")
        self.horizontalLayout.addWidget(self.buttonMinimum)
        self.buttonMaximum = QtWidgets.QPushButton(self.widgetTitleBar)
        self.buttonMaximum.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonMaximum.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("webdings")
        self.buttonMaximum.setFont(font)
        self.buttonMaximum.setObjectName("buttonMaximum")
        self.horizontalLayout.addWidget(self.buttonMaximum)
        self.buttonNormal = QtWidgets.QPushButton(self.widgetTitleBar)
        self.buttonNormal.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonNormal.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("webdings")
        self.buttonNormal.setFont(font)
        self.buttonNormal.setObjectName("buttonNormal")
        self.horizontalLayout.addWidget(self.buttonNormal)
        self.buttonClose = QtWidgets.QPushButton(self.widgetTitleBar)
        self.buttonClose.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonClose.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("webdings")
        self.buttonClose.setFont(font)
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout.addWidget(self.buttonClose)
        self.verticalLayout.addWidget(self.widgetTitleBar)
        self.textEdit = QtWidgets.QTextEdit(FormFrameless)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(FormFrameless)
        QtCore.QMetaObject.connectSlotsByName(FormFrameless)

    def retranslateUi(self, FormFrameless):
        _translate = QtCore.QCoreApplication.translate
        FormFrameless.setWindowTitle(_translate("FormFrameless", "Form"))

        font = QtGui.QFont()
        font.setPointSize(10)

        # create a rect based on passed in args and create a color
        rect = QtCore.QRect(0, 0, 32, 32)
        text_rect = QtCore.QRect(5, 5, 32 - 10, 32 - 10)
        color = QtGui.QColor(155, 118, 67)

        # create a pen and set the color
        pen = QtGui.QPen()
        pen.setColor(color)

        # create a pixmap to paint our image and text on
        pixmap = QtGui.QPixmap(32, 32)

        # create the painter, set the pen, the font, and then draw the image first, then the text on top
        painter = QtGui.QPainter()
        painter.begin(pixmap)
        painter.setPen(pen)
        painter.setFont(font)
        image = QtGui.QImage("./icon.ico")
        painter.drawImage(rect, image)
        painter.drawText(text_rect, QtCore.Qt.TextWordWrap, "text")
        painter.end()

        dir_name = os.getcwd()
        file_name = QtCore.QFile(os.path.join(dir_name, "tooltip.png"))
        file_name.open(QtCore.QIODevice.WriteOnly)
        pixmap.save(file_name, "png")

        tooltip = "<img src = \"" + os.path.join("./tooltip.png") + "\">"


        # self.buttonMinimum.setToolTip(_translate("FormFrameless", "Minimum"))
        self.buttonMinimum.setToolTip(tooltip)
        self.buttonMinimum.setText(_translate("FormFrameless", "0"))
        self.buttonMaximum.setToolTip(_translate("FormFrameless", "Maximum"))
        self.buttonMaximum.setText(_translate("FormFrameless", "1"))
        self.buttonNormal.setToolTip(_translate("FormFrameless", "Normal"))
        self.buttonNormal.setText(_translate("FormFrameless", "2"))
        self.buttonClose.setToolTip(_translate("FormFrameless", "Close"))
        self.buttonClose.setText(_translate("FormFrameless", "r"))
        self.textEdit.setHtml(_translate("FormFrameless",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">frameless window with move and resize</p></body></html>"))


class FramelessWindow(QWidget, Ui_FormFrameless):

    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # 无边框
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setMouseTracking(True)
        # 隐藏还原按钮
        self.buttonNormal.setVisible(False)
        # 标题栏按钮信号
        self.buttonMinimum.clicked.connect(self.showMinimized)
        self.buttonMaximum.clicked.connect(self.showMaximized)
        self.buttonNormal.clicked.connect(self.showNormal)
        self.buttonClose.clicked.connect(self.close)
        self.setStyleSheet('#widgetTitleBar{background: rgb(232, 232, 232);}')

    def changeEvent(self, event):
        """窗口状态改变
        :param event:
        """
        super(FramelessWindow, self).changeEvent(event)
        # 窗口状态改变时修改标题栏控制按钮
        visible = self.isMaximized()
        self.buttonMaximum.setVisible(not visible)
        self.buttonNormal.setVisible(visible)
        if visible:
            self.layout().setContentsMargins(0, 0, 0, 0)
        else:
            # TODO 与UI文件中的布局边距一致
            m = FramelessObject.Margins
            self.layout().setContentsMargins(m, m, m, m)

    def paintEvent(self, event):
        # 透明背景但是需要留下一个透明度用于鼠标捕获
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 255, 1))



if __name__ == '__main__':
    import sys
    import cgitb

    cgitb.enable(format='text')

    app = QApplication(sys.argv)
    if not hasattr(QWindow, 'startSystemMove'):
        QWindow.startSystemResize()
        # 不支持
        QMessageBox.critical(None, '错误', '当前Qt版本不支持该例子')
        QTimer.singleShot(100, app.quit)
    else:
        # 安装全局事件过滤器
        fo = FramelessObject()
        app.installEventFilter(fo)

        w1 = FramelessWindow()
        fo.add_widget(w1)
        w1.show()

        w2 = FramelessWindow()
        fo.add_widget(w2)
        w2.show()
    sys.exit(app.exec_())