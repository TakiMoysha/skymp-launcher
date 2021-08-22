import json

from model.main import Model

class ServerModel(Model):
    def __init__(
        self,
        ip: str,
        port: int,
        data_port: int,
        name: str,
        max_players: int,
        online: int,
    ) -> None:
        self.ip = ip
        self.port = port
        self.data_port = data_port
        self.name = name
        self.max_players = max_players
        self.online = online


    def json(self):
        as_dict = {
            "ip": self.ip,
            "port": self.port,
            "name": self.name,
            "maxPlayers": self.max_players,
            "online": self.online,
        }
        return json.dumps(as_dict)
