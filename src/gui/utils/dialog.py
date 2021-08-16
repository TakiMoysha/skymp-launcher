from qt_core import *

def getExistingDirectoryByFileDialog(dir: str = None):
    """Calls up a window for selecting a folder path"""
    return QFileDialog.getExistingDirectory(None, dir=dir)