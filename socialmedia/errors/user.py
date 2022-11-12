from abc import ABC
from typing import List, Dict, Tuple

from flask import Response

from .base import AppError
from ..responses import get_user_not_found_response, get_user_not_valid_response, get_user_already_exists_response, \
    get_user_unauthenticated_response, get_user_requesting_invalid_id_response, get_user_requesting_another_id_response

__all__ = ['UserNotFoundError', 'UserNotValidError', 'UserUnauthenticatedError', 'UserAlreadyExistsError',
           'UserRequestingInvalidIdError', 'UserRequestingForeignIdError']


class UserError(AppError, ABC):
    """Base error class for user"""
    pass


class UserNotFoundError(UserError):
    """Raised when requesting user doesn't exist in database"""

    def __init__(self, field: str):
        super().__init__()
        self.__field = field

    @property
    def response(self) -> Tuple[Response, int]:
        return get_user_not_found_response(field=self.__field)


class UserNotValidError(UserError):
    """Raised when user data is incorrect.

    Attributes:
        errors (dict) - dictionary of errors (key - invalid field, value - list of error messages)
    """

    def __init__(self, errors: Dict[str, List[str]]):
        super().__init__()
        self.__errors = errors

    @property
    def response(self) -> Tuple[Response, int]:
        return get_user_not_valid_response(errors=self.__errors)


class UserAlreadyExistsError(UserError):
    """Raised when trying to add user to database whose unique fields are already used with another users.

    Attributes:
        fields (list) - list of fields by which user doesn't pass unique validation
    """

    def __init__(self, fields: List[str]):
        super().__init__()
        self.__fields = fields

    @property
    def response(self) -> Tuple[Response, int]:
        return get_user_already_exists_response(fields=self.__fields)


class UserUnauthenticatedError(UserError):
    """Raised when user's credential (password) is invalid"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_user_unauthenticated_response()


class UserRequestingInvalidIdError(UserError):
    """Raised when user is requesting to invalid user id"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_user_requesting_invalid_id_response()


class UserRequestingForeignIdError(UserError):
    """Raised when user is requesting to foreign user id"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_user_requesting_another_id_response()
