import enum

from qt_core import *
from main import *

ORGANIZATION_NAME = "REDHOUSE"
ORGANIZATION_DOMAIN = "REDHOUSE"
APPLICATION_NAME = "SkyMp"

QCoreApplication.setApplicationName(ORGANIZATION_NAME)
QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)

class Settings(MainWindow):
    class SettingsType(enum.Enum):
        skyrim_path = "skyrim_path"


    def __init__(self):
        self.qsettings = QSettings()


    def saveValue(self, key: SettingsType, value: any):
        self.qsettings.setValue(key.value, value)
        self.qsettings.sync()


    def getValue(self, key: SettingsType, default_value: any = None):
        return self.qsettings.value(key.value, default_value)
