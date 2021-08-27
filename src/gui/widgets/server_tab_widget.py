from controllers.theme_manager import Colors, ThemeManager
from qt_core import *

class ServerTabWidget(QTabWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__()
        theme_manager = ThemeManager()

        def getColor(color: Colors): return theme_manager.getColor(color)

        style = f"""
            ServerTabWidget {{
                color: red;
                border: 12px;
            }}
            ServerTabWidget::pane {{
                border: 1px solid black;
                background: white;
            }}
            QWidget {{
                color: {getColor(Colors.background_dark)};
            }}
        """
        style_tab_bar = f"""
            QTabBar::tab:selected {{
                color: white;
            }}

            QTabBar::tab:!selected {{
                color: silver;
            }}

            QTabBar::tab:!selected:hover {{
                background: #999;
            }}

            QTabBar::tab:top:!selected {{
                margin-top: 3px;
            }}
            QTabBar::tab {{
                padding-top: 2px;
                padding-bottom: 2px;
                padding-left: 4px;
                padding-right: 4px;
                border: 1px solid black;
            }}
        """
        self.setStyleSheet("".join([style, style_tab_bar]))
