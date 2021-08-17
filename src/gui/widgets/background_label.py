from qt_core import *

class BackgroundLabel(QLabel):
    def __init__(
        self,
        text = "",
        background_color = "",
        minimum_width = 20,
        maximum_width = 40,
        minimum_height = 25,
        maximum_height = 25,
        text_padding = 2,
        text_color = "rgb(195, 204, 223);",
        alignment = Qt.AlignLeft,
    ):
        super().__init__()
        self.setText(text)
        self.setMinimumHeight(minimum_height)
        self.setMaximumHeight(maximum_height)
        self.setMinimumWidth(minimum_width)
        self.setMaximumWidth(maximum_width)
        self.setAlignment(alignment)

        self.text_padding = text_padding
        self.text_color = text_color
        self.background_color = background_color

        self.setStyle()


    def setStyle(self):
        style = f'''
        BackgroundLabel {{
            color: {self.text_color};
            padding: {self.text_padding};
            background-color: {self.background_color};
        }}
        '''
        self.setStyleSheet(style)