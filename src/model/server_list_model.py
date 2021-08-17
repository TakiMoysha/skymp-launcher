from qt_core import *

class ServerListModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(ServerListModel, self).__init__(*args, **kwargs)
        self.servers = {}

    def data(self):
        pass