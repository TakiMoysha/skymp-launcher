import enum

from main import *
from qt_core import *

ORGANIZATION_NAME = "REDHOUSE"
ORGANIZATION_DOMAIN = "REDHOUSE"
APPLICATION_NAME = "SkyMp"

QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)

class Settings:
    master_servers_list = ["skymp-auth.herokuapp.com", "skyrim-multiplayer.herokuapp.com"]

    class SettingsAttribute(enum.Enum):
        skyrim_path = "skyrim_path"
        theme = "theme"
        master_servers = "master_servers"


    def __init__(self):
        self.qsettings = QSettings()
        master_servers_list = self.getValue(Settings.SettingsAttribute.master_servers)
        if (master_servers_list == None):
            self.saveValue(Settings.SettingsAttribute.master_servers, Settings.master_servers_list)


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
