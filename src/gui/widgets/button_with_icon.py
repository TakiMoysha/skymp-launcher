import os

from gui.widgets.push_button import PushButton
from qt_core import *

from utils import resource_path

class ButtonWithIcon(QPushButton):
    def __init__(
        self,
        text = "",
        height = 30,
        minimum_width = 50,
        text_padding = 20,
        text_color = "red",
        icon_type = "icons",
        icon_name = "",
        icon_color = "rgb(195, 204, 223)",
        btn_color = "rgb(26, 73, 125)",
        btn_hover = "rgb(54, 73, 125)",
        btn_press = "rgb(50, 50, 125)"
    ):
        super().__init__()
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_type = icon_type
        self.icon_name = icon_name
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_press = btn_press

        self.setStyle(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_press = self.btn_press,
        )

        self._setIcon()


    def setStyle(
        self,
        text_padding = 55,
        text_color = "black",
        btn_color = "",
        btn_hover = "",
        btn_press = "",
    ):
        style = f'''
            ButtonWithIcon {{
                color: {text_color};
                background-color: {btn_color};
                padding-left: {text_padding}px;
	            padding-right: {text_padding}px;
                text-align: center;
                border: none;
                border-radius: 8px;
            }}
            ButtonWithIcon:hover {{
                background-color: {btn_hover};
            }}
            ButtonWithIcon:pressed {{
                background-color: {btn_press};
            }}
        '''
        self.setStyleSheet(style)


    def _setIcon(self):
        icon_path = resource_path(
            "/".join(["resources", self.icon_type, self.icon_name])
        )
        icon = QPixmap(icon_path)
        self.setIcon(icon)