import os
import sys
from typing import Union, Callable

APP_PATH = os.path.abspath(os.getcwd())

def resource_path(relative_path):
    """Registers the path to the image so that it is not lost during assembly"""
    if hasattr(sys, "_MEIPASS"):
        os.chdir(sys._MEIPASS)
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(relative_path)


def norm_resource_path(relative_path: str):
    """Call resource_path and replace '\' to  '/'"""
    path = resource_path(relative_path)
    return path.replace('\\', '/')
