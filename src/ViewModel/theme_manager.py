import os

from enum import Enum

# from settings import Settings
import json

from utils import resource_path

class Colors(Enum):
    __slots__ = [
        "text",
        "text_dark",
        "text_light",
        "text_description",
        "icon",
        "transparent",
        "button",
        "button_hover",
        "button_press",
        "background",
        "background_dark",
        "background_light",
        "debug"
    ]

    text = "text"
    text_dark = "text_dark"
    text_light = "text_light"
    text_description = "text_description"
    icon = "icon"
    transparent = "transparent"
    button = "button"
    button_hover = "button_hover"
    button_press = "button_press"
    background = "background"
    background_dark = "background_dark"
    background_light = "background_light"
    debug = "debug"


class ThemeManager:
    class Themes(Enum):
        default = "default"
        dark = "dark"


    def __init__(self, theme_name="default"):
        self.colors = {}

        json_file = resource_path(f"model/themes/{theme_name}.json")
        app_path = os.path.abspath(os.getcwd())
        self.path_to_theme = os.path.normpath(os.path.join(app_path, json_file))

        if not os.path.isfile(self.path_to_theme):
            raise FileNotFoundError(f'{self.path_to_theme} not found')

        self.readThemeFile()


    def readThemeFile(self):
        with open(self.path_to_theme, "r", encoding='utf-8') as reader:
            self.colors = json.loads(reader.read())


    def getColor(self, color_name: Colors) -> str:
        return self.colors.get(color_name.value)



if __name__ == "__main__":
    tm = ThemeManager()
    print(tm.colors)
    print(tm.getColor(Colors.text_light))