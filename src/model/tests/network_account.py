import os

import unittest

import model.network.auth_models as auth_models
import model.network.account as account

EMAIL = os.getenv("EMAIL_TESTS")
LOGIN = os.getenv("LOGIN_TESTS")
PASSWORD = os.getenv("PASSWORD_TESTS")

OK_STATUS = 200


class NetworkAccount(unittest.TestCase):
    def test_login(self):
        login_model = auth_models.ReqLoginModel(
            email=EMAIL,
            password=PASSWORD
        )
        auth_account = account.login(login_model)
        if auth_account.status_code != OK_STATUS:
            print(auth_account.status_code)
            print(auth_account.text)
        self.assertEqual(auth_account.status_code, OK_STATUS)


if __name__ == "__name__":
    try:
        unittest.main()
    except Exception as err:
        print(err)
