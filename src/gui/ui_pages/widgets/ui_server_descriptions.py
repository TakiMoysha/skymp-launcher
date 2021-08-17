from qt_core import *

class UiServerDescriptions(object):
    def setupUi(self, parent_page):
        if not parent_page.objectName():
            parent_page.setObjectName(u"page_home")

        self.label = QLabel()
        self.label.setText("ServerDescriptions")
        self.label.setAlignment(Qt.AlignCenter)