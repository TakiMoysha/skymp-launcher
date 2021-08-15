import os
import sys

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


def isPathToSkyrim(path_to_skyrim: str):
    path = os.path.join(path_to_skyrim, 'SkyrimSELauncher.exe')
    return os.path.isfile(path)


def skyrimHaveSKSE(path_to_skyrim: str):
    path = os.path.join(path_to_skyrim, 'skse64_loader.exe')
    return os.path.isfile(path)
