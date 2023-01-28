from typing import Tuple
from flask import jsonify, Response

from .body import get_request_invalid_content_type_response_body

__all__ = ['get_request_invalid_content_type_response']


def get_request_invalid_content_type_response() -> Tuple[Response, int]:
    return jsonify(get_request_invalid_content_type_response_body()), 400
