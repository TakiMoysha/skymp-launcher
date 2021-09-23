from qt_core import *

class CustomToolTip(QLabel):
    style_tooltip = """
    QLabel {{
        background-color: {dark_one};
        color: {text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        font: 800 9pt "Segoe UI";
    }}
    """
    def __init__(
        self,
        parent,
        tooltip,
        dark_one,
        text_foreground
    ):
        QLabel.__init__(self)

        style = self.style_tooltip.format(
            dark_one = dark_one,
            text_foreground = text_foreground
        )
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(32)
        self.setParent(parent)
        self.setText(tooltip)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)
