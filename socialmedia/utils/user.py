from typing import List, Dict

from socialmedia.api.validators import UserSchema
from ..errors import UserRequestingInvalidIdError, UserRequestingForeignIdError


def get_user_data_errors(user_data: dict, check_missing_data: bool) -> Dict[str, List[str]]:
    return UserSchema(partial=not check_missing_data).validate(user_data)


def get_requesting_id(user_id: str) -> int:
    try:
        return int(user_id)
    except ValueError:
        raise UserRequestingInvalidIdError()


def verify_id_in_token_identity(user_id: str, token_identity: dict) -> int:
    user_id = get_requesting_id(user_id=user_id)
    if user_id == int(token_identity.get('id')):
        return user_id

    raise UserRequestingForeignIdError()
