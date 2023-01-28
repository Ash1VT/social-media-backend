from typing import List, Dict

from socialmedia.api.validators import UserSchema
from ..errors import UserRequestingForeignUserIdError


def get_user_data_errors(user_data: dict, check_missing_data: bool) -> Dict[str, List[str]]:
    return UserSchema(partial=not check_missing_data).validate(user_data)


def get_user_id(token_identity: dict) -> int:
    return int(token_identity.get('id'))


def check_user_operation_permission_on_user(user_id: int, token_identity: dict) -> int:
    if user_id == get_user_id(token_identity=token_identity):
        return user_id

    raise UserRequestingForeignUserIdError()
