from os import path

from settings import Settings, SettingsAttribute

settings = Settings()

# PAHT
SKYRIM_PATH = settings.getValue(SettingsAttribute.skyrim_path)

SKSE_PATH = path.abspath('/'.join([SKYRIM_PATH, 'skse64_loader.exe']))

CLIENT_SETTINGS_PATH = path.abspath(
    '/'.join([SKYRIM_PATH, 'Platform/Plugins/skymp5-client-settings.txt'])
)

# API