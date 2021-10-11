import enum

from qt_core import *

ORGANIZATION_NAME = "REDHOUSE"
ORGANIZATION_DOMAIN = "REDHOUSE"
APPLICATION_NAME = "SkyLauncher"

QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)

class SettingsAttribute(enum.Enum):
    skyrim_path = "skyrim_path"
    theme = "theme"
    remember_account = "remember_account"

    master_servers = "master_servers"
    last_master_server = "last_master_server"
    last_game_server = "last_game_server"


class Settings:
    master_servers_list = ["skymp-auth.herokuapp.com", "skyrim-multiplayer.herokuapp.com"]

    def __init__(self):
        self.qsettings = QSettings()
        if (self.getValue(SettingsAttribute.master_servers) == None):
            self.saveValue(SettingsAttribute.master_servers, Settings.master_servers_list)


    def saveValue(self, key: SettingsAttribute, value: any):
        self.qsettings.setValue(key.value, value)
        self.qsettings.sync()


    def getValue(self, key: SettingsAttribute, default_value: any = None):
        value = self.qsettings.value(key.value, default_value)
        return value


    def addMasterServer(self, master_server_url: str):
        self.qsettings.setValue(
            self.SettingsAttribute.master_servers,
            self.master_servers_list.append(master_server_url)
        )
        self.qsettings.sync()
