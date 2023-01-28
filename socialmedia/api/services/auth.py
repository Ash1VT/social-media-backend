from typing import Tuple

from ..services import UserService
from ...models import User
from ...errors import UserNotValidError, UserUnauthenticatedError
from ...utils import check_password, get_token_jti, create_token_pair, get_user_data_errors

__all__ = ['AuthService']


class AuthService:

    @classmethod
    def login(cls, user_data: dict) -> Tuple[str, str, User]:
        username: str = user_data.get('username')
        password: str = user_data.get('password')
        user = UserService.get_by_username(username=username)

        user_password_hash = user.password_hash
        if not check_password(password=password, hashed_password=user_password_hash):
            raise UserUnauthenticatedError()

        access_token, refresh_token = cls.refresh_tokens(user_id=user.id)
        return access_token, refresh_token, user

    @classmethod
    def register(cls, user_data: dict) -> Tuple[str, str, User]:
        user = UserService.add(user_data=user_data)
        access_token, refresh_token = cls.refresh_tokens(user_id=user.id)
        return access_token, refresh_token, user

    @classmethod
    def refresh_tokens(cls, user_id: int) -> Tuple[str, str]:
        access_token, refresh_token = create_token_pair({'id': user_id})
        access_token_jti = get_token_jti(encoded_token=access_token)
        refresh_token_jti = get_token_jti(encoded_token=refresh_token)

        UserService.update_user_tokens(user_id=user_id, access_token_jti=access_token_jti,
                                       refresh_token_jti=refresh_token_jti)

        return access_token, refresh_token

    @classmethod
    def logout(cls, user_id: int):
        UserService.update_user_tokens(user_id=user_id, access_token_jti=None, refresh_token_jti=None)
