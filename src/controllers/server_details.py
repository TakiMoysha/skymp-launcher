import os
import subprocess

from model.configs.consts import *

def filesInstalled():
    return False


def wrapper_play(master_server: str, game_server_ip: str, game_server_port: int):
    if not is_user_auth(master_server):
        auth_user()
    # TODO: Check files, platform, game
    run_game()


def run_game():
    process = subprocess.Popen([SKSE_PATH], cwd=os.path.dirname(SKSE_PATH))