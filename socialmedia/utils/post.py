from typing import Dict, List

from socialmedia.api.validators import PostSchema
from socialmedia.errors import UserRequestingForeignPostIdError
from .user import get_user_id


def get_post_data_errors(post_data: dict, check_missing_data: bool) -> Dict[str, List[str]]:
    return PostSchema(partial=not check_missing_data).validate(post_data)


def check_user_operation_permission_on_post(post_author_id: int, token_identity: dict) -> int:
    if post_author_id == get_user_id(token_identity=token_identity):
        return post_author_id

    raise UserRequestingForeignPostIdError()
