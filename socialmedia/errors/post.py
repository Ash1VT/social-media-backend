from abc import ABC
from typing import Tuple, List, Dict
from flask import Response

from .base import AppError
from socialmedia.responses import get_post_not_found_response, get_post_not_valid_response, \
    get_user_requesting_foreign_post_id_response, \
    get_post_already_liked_response, get_post_not_liked_response, \
    get_post_already_disliked_response, get_post_not_disliked_response


class PostError(AppError, ABC):
    """Base error class for post"""
    pass


class PostNotFoundError(PostError):
    """Raised when requesting post doesn't exist in database"""

    def __init__(self, field: str):
        super().__init__()
        self.__field = field

    @property
    def response(self) -> Tuple[Response, int]:
        return get_post_not_found_response(field=self.__field)


class PostNotValidError(PostError):
    """Raised when post data is incorrect.

        Attributes:
            errors (dict) - dictionary of errors (key - invalid field, value - list of error messages)
        """

    def __init__(self, errors: Dict[str, List[str]]):
        super().__init__()
        self.__errors = errors

    @property
    def response(self) -> Tuple[Response, int]:
        return get_post_not_valid_response(errors=self.__errors)


class UserRequestingForeignPostIdError(PostError):
    """Raised when user is requesting to posts of another users"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_user_requesting_foreign_post_id_response()


class PostAlreadyLikedError(PostError):
    """Raised when user trying to like post that is already liked"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_post_already_liked_response()


class PostNotLikedError(PostError):
    """Raised when user trying to remove like post that is haven't been liked"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_post_not_liked_response()


class PostAlreadyDislikedError(PostError):
    """Raised when user trying to dislike post that is already disliked"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_post_already_disliked_response()


class PostNotDislikedError(PostError):
    """Raised when user trying to remove dislike post that is haven't been disliked"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_post_not_disliked_response()
