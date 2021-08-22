import os
import unittest

# Tests
from model.tests.network_account import *

EMAIL = os.getenv("EMAIL_TESTS")
LOGIN = os.getenv("LOGIN_TESTS")
PASSWORD = os.getenv("PASSWORD_TESTS")


if __name__ == "__main__":
    unittest.main()