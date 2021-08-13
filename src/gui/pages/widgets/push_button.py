import os

from qt_core import *

class PushButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 40,
        minimum_width = 50,
        text_padding = 55,
        text_color = "rgb(195, 204, 223);",
        icon_name = "",
        icon_color = "rgb(195, 204, 223);",
        btn_color = "rgb(54, 73, 125);",
        btn_hover = "rgb(68, 88, 145);",
        btn_pressed = "rgb(40, 57, 105);",
        is_activate = False
    ):
        super().__init__()
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_name = icon_name
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_activate = is_activate

        self.setStyle(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_activate = self.is_activate
        )


    def setActive(self, is_activate_menu):
        self.setStyle(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_activate = is_activate_menu
        )


    def setStyle(
        self,
        text_padding = 55,
        text_color = "rgb(195, 204, 223);",
        btn_color = "rgb(54, 73, 125);",
        btn_hover = "rgb(68, 88, 145);",
        btn_pressed = "rgb(40, 57, 105);",
        is_activate = False
    ):
        style = f'''
        PushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        PushButton:hover {{
            background-color: {btn_hover};
        }}
        PushButton:pressed {{
            background-color: {btn_pressed};
        }}
        '''

        active_style = f'''
            PushButton {{
                background-color: {btn_color};
                border-right: 5px solid {btn_pressed}
            }}
        '''
        if not is_activate:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet("".join([style, active_style]))


    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.minimum_width, self.height())

        self.drawIcon(painter, self.icon_name, rect, self.icon_color)

        painter.end()


    def drawIcon(self, selfPainter, image_name, rect, color):
        app_path = os.path.abspath(os.getcwd())
        folder = "src/gui/assets/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image_name))

        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        selfPainter.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()
