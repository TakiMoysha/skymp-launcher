import sys
import logging
import traceback

from typing import Optional, Union

from qt_core import *

from main_window import MainWindow
from auth_window import AuthWindow
from splash_screen import SplashScreen

logging.basicConfig(format="%(message)s", level=logging.INFO)

class DialogManager:
    _dialogs: dict[str, list] = {
        "MainWindow": Union[MainWindow, None],
        "AuthWindow": Union[AuthWindow, None],
        "SplashScreen": Union[SplashScreen, None],
    }

    def open(self, name, *args, **kwargs):
        pass


class LauncherApplication(QApplication):
    TMOUT = 30000

    def __init__(self, argv: list[str]) -> None:
        QApplication.__init__(self, argv)
        self._argv = argv


def _run(argv: Optional[list[str]] = None, exec: bool = True):
    global app
    global mw

    app = LauncherApplication(sys.argv)
    mw = MainWindow()
    app.setWindowIcon(QIcon("icon.ico"))

    sys.exit(app.exec())


def run() -> None:
    try:
        _run()
    except Exception as err:
        traceback.print_exc()
        QMessageBox.critical(
            None,
            "Startup Error",
            f"Please notify support of this error:\n\n{traceback.format_exc()}",
        )

run()