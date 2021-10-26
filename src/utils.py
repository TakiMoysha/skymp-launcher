import os
import sys
from typing import Union, Callable

APP_PATH = os.path.abspath(os.getcwd())

def resource_path(relative_path):
    """Registers the path to the image so that it is not lost during assembly"""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


def norm_resource_path(relative_path: str):
    """Call resource_path and replace '\' to  '/'"""
    path = resource_path(relative_path)
    return path.replace('\\', '/')
