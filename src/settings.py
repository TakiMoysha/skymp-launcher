import enum

from qt_core import *

class Settings():
    class SettingsType(enum.Enum):
        skyrim_path = "skyrim_path"

    def __init__(self):
        self.qsettings = QSettings()

    def save_value(self, key: SettingsType, value: any):
        self.qsettings.setValue(key.value, value)
        self.qsettings.sync()


    def get_value(self, key: SettingsType):
        return self.qsettings.value(key.value)
