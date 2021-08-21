import json

from model.main import Model

class SkympClientSettingsModel(Model):
    def __init__(
        self,
        ip: str,
        server_port: int,
        show_me: bool,
        enable_console: bool,
        game_data: object
    ):
        self.ip = ip
        self.server_port = server_port
        self.show_me = show_me
        self.enable_console = enable_console
        self.game_data = game_data


    def json(self):
        as_dict = {
            "ip": self.ip,
            "server-port": self.server_port,
            "show-me": self.show_me,
            "enable-console": self.enable_console,
            "gameData": self.game_data
        }
        return json.dumps(as_dict)