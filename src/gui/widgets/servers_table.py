from qt_core import *

from .server_table_style import style as servers_table_style

class ServersTable(QTableWidget):
    def __init__(
        self,
        radius = 8,
        color = "#FFF",
        bg_color = "#000",
        border_color = "#000",
        context_color = "#0F0F0F",
        selection_color = "#000"
    ):
        super().__init__()

        self.set_style(
            radius = radius,
            color = color,
            bg_color = bg_color,
            border_color = border_color,
            context_color = context_color,
            selection_color = selection_color
        )


    def set_style(
        self,
        radius,
        color,
        bg_color,
        border_color,
        context_color,
        selection_color
    ):
        style = servers_table_style.format(
            border_color = border_color,
            radius = radius,
            bg_color = bg_color,
            color = color,
            context_color = context_color,
            selection_color = selection_color
        )
        self.setStyleSheet(style)