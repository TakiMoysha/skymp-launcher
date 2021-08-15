import os

from qt_core import *

class TitleBarButton(QPushButton):
    def __init__(
        self,
        size = 16,
        border_radius = "8px",
        background_color = "rgb(255, 0, 0)",
        hover_background_color = "rgba(255, 0, 0, 150)"
    ):
        super().__init__()
        self.setMaximumHeight(size)
        self.setMinimumHeight(size)

        self.setMaximumWidth(size)
        self.setMinimumWidth(size)

        self.setStyle(
            border_radius = border_radius,
            background_color = background_color,
            hover_background_color = hover_background_color
        )


    def setStyle(
        self,
        border_radius = "8px",
        background_color = "rgb(255, 0, 0)",
        hover_background_color = "rgba(255, 0, 0, 150)"
    ):
        style = f'''
        QPushButton {{
            border: none;
            border-radius: {border_radius};
            background-color: {background_color};
        }}
        QPushButton:hover {{
            background-color: {hover_background_color};
        }}
        '''
        self.setStyleSheet(style)
