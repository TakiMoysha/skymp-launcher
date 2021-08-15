from qt_core import *

def getDirectory():
    """Calls up a window for selecting a folder path"""
    return QFileDialog.getExistingDirectory(None)