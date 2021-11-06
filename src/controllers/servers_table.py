from PySide6.QtCore import QObject, Signal
import requests
import json

import ping3


# global
servers_list = []
gl_master_server = None

class WGetActiveGameServers(QObject):
    finished = Signal()
    result = Signal(tuple)

    def __init__(self, master_server) -> None:
        super().__init__()
        global gl_master_server, servers_list
        servers_list = []
        gl_master_server = master_server

    def run(self):
        game_servers = get_active_game_servers_and_load_details(gl_master_server)
        self.result.emit(game_servers)
        self.finished.emit()


class GameServer():
    __slots__ = (
        'master_server', 'ip_address', 'port', 'name_server', 'icon_url',
        'desc', 'mods', 'dlls'
    )

    def __init__(self, master_server: str, ip_address: str, port: int, name_server: str,
            icon_url: str, descriptions: str, mods: list, dlls: list
        ) -> None:
        self.master_server = master_server
        self.ip_address = ip_address
        self.port = port
        self.name_server = name_server
        self.icon_url = icon_url
        self.desc = descriptions
        self.mods = mods
        self.dlls = dlls


def get_active_game_servers_and_load_details(master_server: str) -> tuple:
    session = requests.Session()
    url = f'http://{master_server}/api/servers/'
    try:
        game_servers = json.loads(session.get(url).text)
    except Exception as err:
        print(err)
    result = []
    def game_server_to_list(game_server_object):
        server = [
            (game_server_object.get('name')),
            (int(ping3.ping(game_server_object.get('ip'), unit='ms'))),
            (f"{game_server_object.get('online')}/{game_server_object.get('maxPlayers')}")
        ]
        return server

    def load_details(master_server, game_server_name, game_server_ip, game_server_port):
        url = f'http://{game_server_ip}:{game_server_port+1}'
        desc_url = f'{url}/desc.txt'
        icon_url = f'{url}/servericon.png'
        manifest_url = f'{url}/manifest.json'

        try:
            server_desc = session.get(desc_url).text
            manifest = json.loads(session.get(manifest_url).text)
            mods_list = manifest.get('loadOrder')
        except Exception as err:
            print(err)

        dlls_list = []

        gs = GameServer(
            master_server, game_server_ip, game_server_port, game_server_name, icon_url,
            server_desc, mods_list, dlls_list
        )
        servers_list.append(gs)

    for server_object in game_servers:
        game_server = game_server_to_list(server_object)
        server_name, *_ = game_server
        load_details(master_server, server_name, server_object.get('ip'), server_object.get('port'))
        result.append(game_server)

    return tuple(result)


def get_details_by_server_index(index: int):
    game_server = servers_list[index]
    return game_server