import os

from enum import Enum

# from settings import Settings
import json

class ThemeManager:

    class Colors(Enum):
        text = "text"
        text_dark = "text_dark"
        text_light = "text_light"
        text_description = "text_description"
        icon = "icon"
        button = "button"
        button_hover = "button_hover"
        button_press = "button_press"
        background_base = "background_base"
        background_light = "background_light"


    class Themes(Enum):
        default = "default"
        dark = "dark"


    def __init__(self):
        self.colors = {}

        theme_name = "default"
        json_file = f"model/themes/{theme_name}.json"
        app_path = os.path.abspath(os.getcwd())
        self.path_to_theme = os.path.normpath(os.path.join(app_path, json_file))

        if not os.path.isfile(self.path_to_theme):
            raise FileNotFoundError(f'{self.path_to_theme} not found')

        self.readThemeFile()


    def readThemeFile(self):
        with open(self.path_to_theme, "r", encoding='utf-8') as reader:
            self.colors = json.loads(reader.read())


    def getColor(self, color_name: Colors):
        print(self.colors)
        return self.colors.get(color_name.value)



if __name__ == "__main__":
    tm = ThemeManager()
    print(tm.getColor(ThemeManager.Colors.text_light))