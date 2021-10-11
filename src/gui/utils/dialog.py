from typing import Union
from gui.utils.qt import qconnect

from qt_core import *

def getExistingDirectoryByFileDialog(dir: str):
    """Calls up a window for selecting a folder path"""
    return QFileDialog.getExistingDirectory(None, dir=dir)


def showCriticalMessage(parent: QWidget, text: str):
    _showText(parent, text, cupyBtn=True)


def showWarningMessage(parent: QWidget, text: str):
    _showText(parent, text, cupyBtn=True)


def showInfoMessage(parent: QWidget, text: str):
    _showText(parent, text)


def _showText(
    parent: QWidget,
    txt: str,
    type: str = "text",
    run: bool = True,
    minWidth: int = 500,
    minHeight: int = 400,
    title: str = "Launcher",
    copyBtn: bool = False,
    plainTextEdit: bool = False,
) -> tuple[QDialog, QDialogButtonBox]:
    """Calls dialog with text and buttons"""
    diag = QDialog(parent)
    diag.setWindowTitle(title)
    layout = QVBoxLayout(diag)
    diag.setLayout(layout)
    text: Union[QPlainTextEdit, QTextBrowser]
    if plainTextEdit:
        text = QPlainTextEdit()
        text.setReadOnly(True)
        text.setWordWrapMode(QTextOption.NoWrap)
        text.setPlainText(txt)
    else:
        text = QTextBrowser()
        text.setOpenExternalLinks(True)
        if type == "text":
            text.setPlainText(txt)
        else:
            text.setHtml(txt)
    layout.addWidget(text)
    box = QDialogButtonBox(QDialogButtonBox.Close)
    layout.addWidget(box)
    if copyBtn:
        def onCopy() -> None:
            QApplication.clipboard().setText(text.toPlainText())

        btn = QPushButton()
        btn.setText("Copy")
        qconnect(btn.clicked, onCopy)
        box.addButton(btn, QDialogButtonBox.ActionRole)

    diag.setMinimumHeight(minHeight)
    diag.setMinimumWidth(minWidth)
    if run:
        diag.exec_()
        return None
    else:
        return diag, box