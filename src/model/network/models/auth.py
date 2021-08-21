import json

from model.main import Model

class ReqLoginModel(Model):
    def __init__(self, email, password):
        self.email = email
        self.password = password


class ReqRegisterModel(Model):
    def __init__(self, email: str, name: str, password: str):
        self.email = email
        self.name = name
        self.password = password


class ReqResetPassword(Model):
    def __init__(self, email: str):
        self.email = email


class ReqVerifyRegisterModel(Model):
    def __init__(self, id: int, email: str, password: str, pin: str):
        self.id = id
        self.email = email
        self.password = password
        self.pin = pin




class ResLoginModel(Model):
    def __init__(self, id: str, token: str) -> None:
        self.id = id
        self.token = token


class ResRegisterModel(Model):
    def __init__(self, id: str) -> None:
        self.id = id


class ResVerifyRegisterModel(Model):
    def __init__(self, token: str) -> None:
        self.token = token