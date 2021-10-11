import os
import subprocess

from model.configs.consts import *

from .servers_table import servers_list

def get_game_server_by_name(name: str):
    for server in servers_list:
        if server.get("name") == name:
            return server
    return None


def get_details_by_server_name(name: str):
    game_server = get_game_server_by_name(name)
    if game_server == None: return
    # todo: download info
    print(game_server)
    server_details = {
        'logo': "",
        'name': "",
        'address': "",
        'desc': "",
        'mods': "",
    }
    return server_details


def filesInstalled():
    return False

def wrapper_play(master_server: str, game_server_ip: str, game_server_port: int):
    if not is_user_auth(master_server):
        auth_user()
    # TODO: Check files, platform, game
    run_game()


def run_game():
    process = subprocess.Popen([SKSE_PATH], cwd=os.path.dirname(SKSE_PATH))