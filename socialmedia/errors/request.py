from abc import ABC
from typing import Tuple

from flask import Response

from .base import AppError
from ..responses import get_request_invalid_content_type_response

__all__ = ['RequestInvalidContentTypeError']


class RequestError(AppError, ABC):
    """Base error class for requests"""
    pass


class RequestInvalidContentTypeError(RequestError):
    """Raised when request has invalid content-type"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_request_invalid_content_type_response()
