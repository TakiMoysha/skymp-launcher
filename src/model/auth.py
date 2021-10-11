import requests

def authorization(email: str, password: str):
    auth_form = {
        "email": email,
        "password": password
    }
    server_address = ''
    r = requests.post(f'https://{server_address}/users/:id/auth', data=auth_form)
    result = {
        "token": "Json Web Token here",
        "gameDataToken": "Не уверен что это настоящий токен, скорее ключ"
    }