from qt_core import *
from typing import Callable, Union

def qconnect(signal: Union[Callable], func: Callable) -> None:
    "Helper to work around type checking not working with signal.connect(func)."
    signal.connect(func)


def delegateToThread(Worker: QObject) -> None:
    """Create thread and put to worker(QObject)"""
    thread = QThread()
    worker = Worker()

    worker.moveToThread(thread)

    thread.started.connect(worker.run)
    thread.finished.connect(worker.deleteLater)

    worker.finished.connect(thread.quit)
    worker.finished.connect(thread.deleteLater)

    thread.start()