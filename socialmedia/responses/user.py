from typing import Tuple, List, Dict

from flask import Response, jsonify

from .body import get_user_response_body, get_current_user_response_body, \
    get_update_user_response_body, get_patch_user_response_body, get_delete_user_response_body, \
    get_user_not_found_response_body, get_user_not_valid_response_body, get_user_already_exists_response_body, \
    get_user_unauthenticated_response_body, get_user_requesting_invalid_id_response_body, \
    get_user_requesting_another_id_response_body, get_all_users_response_body
from ..models import User

__all__ = ['get_user_response', 'get_all_users_response', 'get_current_user_response',
           'get_update_user_response', 'get_patch_user_response', 'get_delete_user_response',
           'get_user_not_found_response', 'get_user_not_valid_response', 'get_user_already_exists_response',
           'get_user_unauthenticated_response', 'get_user_requesting_invalid_id_response',
           'get_user_requesting_another_id_response']


def get_user_response(user: User) -> Tuple[Response, int]:
    return jsonify(get_user_response_body(user=user)), 200


def get_all_users_response(users: List[User]) -> Tuple[Response, int]:
    return jsonify(get_all_users_response_body(users=users)), 200


def get_current_user_response(user: User) -> \
        Tuple[Response, int]:
    return jsonify(get_current_user_response_body(user=user)), 200


def get_update_user_response() -> Tuple[Response, int]:
    return jsonify(get_update_user_response_body()), 200


def get_patch_user_response() -> Tuple[Response, int]:
    return jsonify(get_patch_user_response_body()), 200


def get_delete_user_response() -> Tuple[Response, int]:
    return jsonify(get_delete_user_response_body()), 200


def get_user_not_found_response(field: str) -> Tuple[Response, int]:
    return jsonify(get_user_not_found_response_body(field=field)), 400


def get_user_not_valid_response(errors: Dict[str, List[str]]) -> Tuple[Response, int]:
    return jsonify(get_user_not_valid_response_body(errors=errors)), 400


def get_user_already_exists_response(fields: List[str]) -> Tuple[Response, int]:
    return jsonify(get_user_already_exists_response_body(fields=fields)), 400


def get_user_unauthenticated_response() -> Tuple[Response, int]:
    return jsonify(get_user_unauthenticated_response_body()), 401


def get_user_requesting_invalid_id_response() -> Tuple[Response, int]:
    return jsonify(get_user_requesting_invalid_id_response_body()), 400


def get_user_requesting_another_id_response() -> Tuple[Response, int]:
    return jsonify(get_user_requesting_another_id_response_body()), 403
