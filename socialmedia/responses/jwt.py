from typing import Tuple, Dict
from flask import jsonify, Response

from .body import get_token_expired_response_body, get_token_missing_response_body, get_token_invalid_response_body, \
    get_token_revoked_response_body

__all__ = ['get_token_expired_response', 'get_token_missing_response', 'get_token_invalid_response',
           'get_token_revoked_response']


def get_token_expired_response(token_header: Dict, token_payload: Dict) -> Tuple[Response, int]:
    return jsonify(get_token_expired_response_body()), 401


def get_token_missing_response(message: str) -> Tuple[Response, int]:
    return jsonify(get_token_missing_response_body(message=message)), 401


def get_token_invalid_response(message: str) -> Tuple[Response, int]:
    return jsonify(get_token_invalid_response_body(message=message)), 401


def get_token_revoked_response(token_header: Dict, token_payload: Dict) -> Tuple[Response, int]:
    return jsonify(get_token_revoked_response_body()), 401
