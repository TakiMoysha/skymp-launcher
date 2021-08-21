# Static Class
import os

from model.enums.locales import Locales
from model.configs.classes import SecureString

Loaded = False

# Skyrim
PathToSkyrim: str = None
PathToSkympClientSettings: str = os.path.abspath(
    f"{PathToSkyrim}/Data/Plarform/Plugins/skymp5-client-settings.txt"
)
PathToSkyrimTmp: str = os.path.abspath(f"{PathToSkyrim}/tmp/")
PathToSkyrimMods: str = os.path.abspath(f"{PathToSkyrim}/Mods/")


# Launcher
LastVersion: str = None
LastSertverID: int = None
FavoriteServers: list = None
Locale: Locales = None
ExperimentalFunctions: bool = False


# User
UserID: int = None
UserName: str = None
RememberMe: bool = None
userToken: SecureString = None
UserToken: str = None


@staticmethod
def Load():
    pass


@staticmethod
def Save():
    pass


@staticmethod
def Reset():
    pass
