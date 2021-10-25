import sys

import requests
from PySide2 import QtCore, QtGui, QtWidgets

DOWNLOAD_URL = 'http://www.gutenberg.org/cache/epub/10/pg10.txt'
class ProgressIndicator(QtWidgets.QProgressBar):
    def __init__(self, parent=None):
        super(ProgressIndicator, self).__init__(parent)

        self.setMinimum(0)
        self.setMaximum(0)


class DisplayWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DisplayWidget, self).__init__(parent)

        self._layout = QtWidgets.QVBoxLayout(self)
        self._textarea = QtWidgets.QPlainTextEdit()
        self._textarea.setReadOnly(True)
        self._layout.addWidget(self._textarea)
        self._button = QtWidgets.QPushButton('Download')
        self._button.clicked.connect(self._button_clicked)
        self._layout.addWidget(self._button)
        self._progress = ProgressIndicator()
        self._layout.addWidget(self._progress)

    def _button_clicked(self):
        pass

import time
def parse_html():
    time.sleep(0.01)

class RunnableWithSignals(QtCore.QObject, QtCore.QRunnable):
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        QtCore.QRunnable.__init__(self, parent)


class DownloadData(RunnableWithSignals):
    finished = QtCore.Signal(str)

    def run(self):
        response = requests.get(DOWNLOAD_URL)
        parse_html()
        self.finished.emit(response.text)


class MyWidget(DisplayWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)

        self._thread_pool = QtCore.QThreadPool.globalInstance()

    def _button_clicked(self):
        runnable = DownloadData()
        runnable.finished.connect(self._populate_textarea)
        self._thread_pool.start(runnable)

    def _populate_textarea(self, text):
        self._textarea.setPlainText(text)


def main(argv):
    app = QtWidgets.QApplication(argv)
    w = MyWidget()
    w.show()
    w.raise_()
    return app.exec_()


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))