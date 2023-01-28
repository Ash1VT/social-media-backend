from abc import ABC
from typing import Tuple, List, Dict
from flask import Response

from .base import AppError
from socialmedia.responses import get_comment_not_found_response, get_comment_not_valid_response, \
    get_user_requesting_foreign_comment_id_response, \
    get_comment_already_liked_response, get_comment_not_liked_response, \
    get_comment_already_disliked_response, get_comment_not_disliked_response


class CommentError(AppError, ABC):
    """Base error class for comment"""
    pass


class CommentNotFoundError(CommentError):
    """Raised when requesting comment doesn't exist in database"""

    def __init__(self, field: str):
        super().__init__()
        self.__field = field

    @property
    def response(self) -> Tuple[Response, int]:
        return get_comment_not_found_response(field=self.__field)


class CommentNotValidError(CommentError):
    """Raised when comment data is incorrect.

        Attributes:
            errors (dict) - dictionary of errors (key - invalid field, value - list of error messages)
        """

    def __init__(self, errors: Dict[str, List[str]]):
        super().__init__()
        self.__errors = errors

    @property
    def response(self) -> Tuple[Response, int]:
        return get_comment_not_valid_response(errors=self.__errors)


class UserRequestingForeignCommentIdError(CommentError):
    """Raised when user is requesting to comments of another users"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_user_requesting_foreign_comment_id_response()


class CommentAlreadyLikedError(CommentError):
    """Raised when user trying to like comment that is already liked"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_comment_already_liked_response()


class CommentNotLikedError(CommentError):
    """Raised when user trying to remove like comment that is haven't been liked"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_comment_not_liked_response()


class CommentAlreadyDislikedError(CommentError):
    """Raised when user trying to dislike comment that is already disliked"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_comment_already_disliked_response()


class CommentNotDislikedError(CommentError):
    """Raised when user trying to remove dislike comment that is haven't been disliked"""

    @property
    def response(self) -> Tuple[Response, int]:
        return get_comment_not_disliked_response()
