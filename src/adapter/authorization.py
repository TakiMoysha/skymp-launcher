from model.auth.auth_model import AuthModel
from model.auth.reg_model import RegModel
from model.auth.rec_pswrd_model import RecPswrdModel


class Authorization:
    def __init__(self):
        self.auth_model = AuthModel()
        self.reg_model = RegModel()
        self.pswrd_model = RecPswrdModel()