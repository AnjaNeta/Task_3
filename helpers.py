import requests
import uuid
from urls import API_REGISTER_URL, API_LOGIN_URL, API_USER_URL


def generate_random_user():
    """Генерирует данные случайного пользователя с использованием uuid."""
    unique_id = str(uuid.uuid4())[:8]
    return {
        "email": f"test_{unique_id}@example.com",
        "password": f"Pass_{unique_id}",
        "name": f"User_{unique_id}"
    }


def create_user(payload):
    """Создаёт пользователя через API."""
    response = requests.post(API_REGISTER_URL, json=payload)
    return response


def login_user(email, password):
    """Авторизует пользователя через API."""
    payload = {"email": email, "password": password}
    response = requests.post(API_LOGIN_URL, json=payload)
    return response


def delete_user(access_token):
    """Удаляет пользователя по токену."""
    headers = {'Authorization': access_token}
    response = requests.delete(API_USER_URL, headers=headers)
    return response

    