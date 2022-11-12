from typing import List, Dict

from socialmedia.models import User
from socialmedia.constants import USER_NOT_FOUND_ERROR_STRING, \
    USER_NOT_VALID_ERROR_STRING, USER_ALREADY_EXISTS_ERROR_STRING, USER_UNAUTHENTICATED_ERROR_STRING, \
    USER_REQUESTING_INVALID_ID_ERROR_STRING, USER_REQUESTING_ANOTHER_ID_ERROR_STRING, \
    DEFAULT_ERROR_RESPONSE, DEFAULT_SUCCESS_RESPONSE

__all__ = ['get_user_response_body', 'get_all_users_response_body', 'get_current_user_response_body',
           'get_update_user_response_body', 'get_patch_user_response_body', 'get_delete_user_response_body',
           'get_user_not_found_response_body', 'get_user_not_valid_response_body',
           'get_user_already_exists_response_body', 'get_user_unauthenticated_response_body',
           'get_user_requesting_invalid_id_response_body', 'get_user_requesting_another_id_response_body']


def get_user_response_body(user: User) -> Dict:
    return {'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email
            }


def get_all_users_response_body(users: List[User]) -> List:
    return [
        {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email
        } for user in users
    ]


def get_current_user_response_body(user: User) -> Dict:
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email
    }


def get_update_user_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_patch_user_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_delete_user_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_user_not_found_response_body(field: str) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': USER_NOT_FOUND_ERROR_STRING,
        'field': field
    }


def get_user_not_valid_response_body(errors: Dict[str, List[str]]) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': USER_NOT_VALID_ERROR_STRING,
        'fields': list(errors.keys()),
        'errors': errors
    }


def get_user_already_exists_response_body(fields: List[str]) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': USER_ALREADY_EXISTS_ERROR_STRING,
        'fields': fields
    }


def get_user_unauthenticated_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': USER_UNAUTHENTICATED_ERROR_STRING,
        'field': 'password'
    }


def get_user_requesting_invalid_id_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': USER_REQUESTING_INVALID_ID_ERROR_STRING
    }


def get_user_requesting_another_id_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': USER_REQUESTING_ANOTHER_ID_ERROR_STRING
    }
