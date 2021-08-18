import os
import sys
from typing import Union, Callable

APP_PATH = os.path.abspath(os.getcwd())

def resource_path(relative):
    """Registers the path to the image so that it is not lost during assembly"""
    if hasattr(sys, "_MEIPASS"):
        os.chdir(sys._MEIPASS)
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def norm_resource_path(relative: str):
    """Call resource_path and replace '\' to  '/'"""
    path = resource_path(relative)
    return path.replace('\\', '/')
