from typing import Dict, List

from socialmedia.api.validators import CommentSchema
from socialmedia.errors import UserRequestingForeignCommentIdError
from .user import get_user_id


def get_comment_data_errors(comment_data: dict, check_missing_data: bool) -> Dict[str, List[str]]:
    return CommentSchema(partial=not check_missing_data).validate(comment_data)


def check_user_operation_permission_on_comment(comment_author_id: int, token_identity: dict) -> int:
    if comment_author_id == get_user_id(token_identity=token_identity):
        return comment_author_id

    raise UserRequestingForeignCommentIdError()
