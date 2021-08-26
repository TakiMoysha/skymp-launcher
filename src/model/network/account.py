import socket
import requests
from requests.api import request

import model.configs.settings as Settings
from model.network.auth_models import \
    ReqLoginModel, ReqRegisterModel, ReqResetPassword, ReqVerifyRegisterModel, \
    ResLoginModel, ResRegisterModel, ResVerifyRegisterModel


_URL_API = "https://skymp.io/api/"

def register(model: ReqRegisterModel):
    raw = requests.post(f"{_URL_API}users", data=model.json())
    return raw


def login(model: ReqLoginModel):
    raw = requests.post(f"{_URL_API}users/login", data=model.json())
    return raw


def verify(model: ReqVerifyRegisterModel):
    raw = requests.post(f"{_URL_API}users/login", data=model.json())
    return raw


def reset_password(model: ReqResetPassword):
    raw = requests.post(f"{_URL_API}users/reset-password", data=model.json())
    return raw


def verify_token():
    raw = requests.get(f"{_URL_API}secure")
    return raw


def get_login():
    raw = requests.get(f"{_URL_API}users/{Settings.UserId}")
    return raw


def get_session(address: str):
    raw = requests.post(f"{_URL_API}users/{Settings.UserId}/play/{address}")
    return raw


def internal_request(url: str, method: str, auth: bool, data: str):
    try:
        return request(method=method, url=url, auth=auth, data=data)
    except Exception as err:
        print(err)
    return None
