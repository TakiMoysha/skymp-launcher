from qt_core import *

class ServersTableModel(QAbstractTableModel):
    def __init__(self, parent, servers_list, header, *args):
        super.__init__(self, parent, *args)