import requests

desc = "desc.txt"
servericon = "servericon.png"
manifest = "manifest.json"

class GameServer:
    def __init__(self, ip, port, name, maxPlayers, online) -> None:
        self.ip = ip
        self.port = port
        self.name = name
        self.maxPlayers = maxPlayers
        self.online = online

    def download_details(self):
        url = f"http://{self.ip}:{self.port + 1}/"
        self.descriptions = requests.get(''.join([url, desc]))
        self.icon = requests.get(''.join([url, servericon]))
        self.mods = requests.get(''.join([url, manifest]))