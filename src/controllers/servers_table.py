import logging
from time import sleep
from PySide6.QtCore import QObject, Signal
import requests
import json

# global servers_list
servers_list = []

class WGetActiveGameServers(QObject):
    finished = Signal()
    result = Signal(tuple)

    def __init__(self, master_server) -> None:
        super().__init__()
        self.master_server = master_server


    def run(self):
        # servers = get_active_game_servers(master_server)
        servers = get_active_game_servers(self.master_server)
        self.result.emit(servers)
        # sleep(2)
        self.finished.emit()


def get_active_game_servers(master_server: str) -> tuple:
    response = json.loads(requests.get(f'https://{master_server}/api/servers/').text)
    result = []

    for server_object in response:
        servers_list.append(server_object)
        server = []
        server.append(server_object.get('name'))
        server.append(123)
        server.append(f"{server_object.get('online')}/{server_object.get('maxPlayers')}")
        result.append(server)

    return tuple(result)


