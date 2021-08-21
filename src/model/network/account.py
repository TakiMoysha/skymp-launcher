import socket
import requests
from requests.api import request

import model.configs.settings as Settings
from model.network.models.auth import \
    ReqLoginModel, ReqRegisterModel, ReqResetPassword, ReqVerifyRegisterModel, \
    ResLoginModel, ResRegisterModel, ResVerifyRegisterModel


URL_API = "https://skymp.io/api"

def register(model: ReqRegisterModel):
    raw = requests.post(f"{URL_API}users")
    print(raw.json())


def login(model: ReqLoginModel):
    raw = requests.post(f"{URL_API}users/login")
    print(raw.json())


def verify(model: ReqVerifyRegisterModel):
    raw = requests.post(f"{URL_API}users/login")
    print(raw.json())


def reset_password(model: ReqResetPassword):
    raw = requests.post(f"{URL_API}users/reset-password")
    print(raw.json())


def verify_token():
    return requests.get(f"{URL_API}secure")


def get_login():
    raw = requests.get(f"{URL_API}users/{Settings.UserId}")


def get_session(address: str):
    raw = requests.post(f"{URL_API}users/{Settings.UserId}/play/{assress}")


def internal_request(url: str, method: str, auth: bool, data: str):
    try:
        return request(method=method, url=url, auth=auth, data=data)
    except Exception as err:
        print(err)
    return None
