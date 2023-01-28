from typing import Tuple
from flask import jsonify, Response

from .body import get_login_response_body, get_register_response_body, get_refresh_response_body, \
    get_logout_response_body
from socialmedia.models.dto_models import UserDto

__all__ = ['get_login_response', 'get_register_response', 'get_refresh_response', 'get_logout_response']


def get_login_response(user: UserDto) -> Tuple[Response, int]:
    return jsonify(get_login_response_body(user=user)), 200


def get_register_response(user: UserDto) -> Tuple[Response, int]:
    return jsonify(get_register_response_body(user=user)), 200


def get_refresh_response() -> Tuple[Response, int]:
    return jsonify(get_refresh_response_body()), 200


def get_logout_response() -> Tuple[Response, int]:
    return jsonify(get_logout_response_body()), 200
