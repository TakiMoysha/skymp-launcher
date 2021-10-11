from controllers.theme_manager import Colors, ThemeManager
from qt_core import *

from .server_tab_widget_style import server_tab_style

class ServerDetailsTabWidget(QTabWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__()
        theme_manager = ThemeManager()

        def getColor(color: Colors): return theme_manager.getColor(color)

        self.setStyleSheet(server_tab_style.format(
            _tab_border_color=getColor(Colors.text_dark),
            _tab_selected=getColor(Colors.button_press),
            _tab_color=getColor(Colors.button),
            _text_color=getColor(Colors.text),
            _background_color=getColor(Colors.background),
            _border_view=getColor(Colors.button_press)
        ))

