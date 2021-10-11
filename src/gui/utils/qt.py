from qt_core import *
from typing import Callable, Union

def qconnect(signal: Union[Callable], func: Callable) -> None:
    "Helper to work around type checking not working with signal.connect(func)."
    signal.connect(func)