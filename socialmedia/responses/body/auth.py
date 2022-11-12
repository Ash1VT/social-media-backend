from typing import Dict

from socialmedia.models import User
from socialmedia.constants import DEFAULT_SUCCESS_RESPONSE

__all__ = ['get_login_response_body', 'get_register_response_body', 'get_refresh_response_body',
           'get_logout_response_body']


def get_login_response_body(user: User) -> Dict:
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email
    }


def get_register_response_body(user: User) -> Dict:
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email
    }


def get_refresh_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_logout_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE
