from typing import Dict

from socialmedia.constants import DEFAULT_ERROR_RESPONSE

__all__ = ['get_token_expired_response_body', 'get_token_missing_response_body', 'get_token_invalid_response_body',
           'get_token_revoked_response_body']


def get_token_expired_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': 'Token is expired'
    }


def get_token_missing_response_body(message: str) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': message
    }


def get_token_invalid_response_body(message: str) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': message
    }


def get_token_revoked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': 'Revoked token is encountered'
    }
