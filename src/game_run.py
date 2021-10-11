import os
import subprocess
import time

from model.configs.consts import *

from pymem import Pymem

# from my_code import imgui_code
code = """
filepath = os.path.abspath("D:\Documents\Coding\python-skymp-launcher\out.txt")
with open(filepath, "w+") as file:
    file.write("asd")
"""
def inject_code():
    filepath = os.path.abspath("D:\Documents\Coding\python-skymp-launcher\out.txt")
    try:
        import os
        data = os.getpid()
    except Exception as err:
        data = err
    finally:
        with open(filepath, "w+") as file:
            file.write(data)

def run_game():
    process = subprocess.Popen([SKSE_PATH], cwd=os.path.dirname(SKSE_PATH))
    time.sleep(5)
    print(process.stdout)
    print(process.stderr)
    print(process.stdin)
    process.stdout.readline()


def show_all_included_modules(pm):
    modules = list(pm.list_modules())
    for module in modules:
        print(module.name)


def run_game_with_inject():
    skyrim_process = subprocess.Popen([SKSE_PATH], cwd=os.path.dirname(SKSE_PATH))

    time.sleep(3)
    pm = Pymem("SkyrimSE.exe")
    pm.inject_python_interpreter()
    code = ""
    pm.inject_python_shellcode(code)


if __name__ == "__main__":
    run_game()