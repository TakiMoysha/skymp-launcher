import requests
import json

# global servers_list
servers_list = []

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


