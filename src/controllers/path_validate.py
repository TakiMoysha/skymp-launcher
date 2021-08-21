import os
import sys


def isPathToSkyrim(path_to_skyrim: str):
    path = os.path.join(path_to_skyrim, 'SkyrimSELauncher.exe')
    return os.path.isfile(path)


def skyrimHaveSKSE(path_to_skyrim: str):
    path = os.path.join(path_to_skyrim, 'skse64_loader.exe')
    return os.path.isfile(path)
