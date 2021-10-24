import requests




def login_user(master_server: str, email: str, password: str) -> dict:
    url = f'https://{master_server}/api/users/login/'
    params = {
        "email": email,
        "password": password
    }

    response = requests.post(url, params=params)
    if response.status_code != 200: return {}
    return response.json()


def logout():
    pass


def registration():
    pass


def reset_password():
    pass