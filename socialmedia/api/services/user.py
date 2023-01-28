from typing import List, Optional

from ..repositories import UserRepository
from ...models import User
from ...errors import UserNotFoundError, UserNotValidError, UserAlreadyExistsError
from ...utils import hash_password, get_user_data_errors

__all__ = ['UserService']


class UserService:

    @classmethod
    def get_all(cls) -> List[User]:
        return UserRepository.get_all()

    @classmethod
    def get_by_username(cls, username: str) -> User:
        user = UserRepository.get_by_username(username=username)

        if not user:
            raise UserNotFoundError(field=User.username.name)

        return user

    @classmethod
    def get_by_email(cls, email: str) -> User:
        user = UserRepository.get_by_email(email=email)

        if not user:
            raise UserNotFoundError(field=User.email.name)

        return user

    @classmethod
    def get_by_id(cls, user_id: int) -> User:
        user = UserRepository.get_by_id(user_id=user_id)

        if not user:
            raise UserNotFoundError(field=User.id.name)

        return user

    @classmethod
    def add(cls, user_data: dict) -> User:
        errors = get_user_data_errors(user_data=user_data, check_missing_data=True)

        if len(errors):
            raise UserNotValidError(errors=errors)

        first_name: str = user_data.get('first_name')
        last_name: str = user_data.get('last_name')
        username: str = user_data.get('username')
        email: str = user_data.get('email')
        password: str = user_data.get('password')

        password_hash: str = hash_password(password=password)

        exist_field_names = list()
        if cls.exists_with_username(username=username):
            exist_field_names.append(User.username.name)
        if cls.exists_with_email(email=email):
            exist_field_names.append(User.email.name)

        if len(exist_field_names):
            raise UserAlreadyExistsError(fields=exist_field_names)

        return UserRepository.add(first_name=first_name, last_name=last_name, username=username,
                                  email=email, password_hash=password_hash)

    @classmethod
    def update(cls, user_id: int, user_data: dict) -> User:
        if not cls.exists_with_id(user_id=user_id):
            raise UserNotFoundError(field=User.id.name)

        errors = get_user_data_errors(user_data=user_data, check_missing_data=True)
        if len(errors):
            raise UserNotValidError(errors=errors)

        first_name: str = user_data.get('first_name')
        last_name: str = user_data.get('last_name')
        username: str = user_data.get('username')
        email: str = user_data.get('email')
        password: str = user_data.get('password')

        password_hash: str = hash_password(password=password)

        exist_field_names = list()
        if cls.exists_with_username(username=username):
            exist_field_names.append(User.username.name)
        if cls.exists_with_email(email=email):
            exist_field_names.append(User.email.name)

        if len(exist_field_names):
            raise UserAlreadyExistsError(fields=exist_field_names)

        return UserRepository.update(user_id=user_id, first_name=first_name, last_name=last_name,
                                     username=username, email=email, password_hash=password_hash)

    @classmethod
    def patch(cls, user_id: int, user_data: dict) -> User:
        if not cls.exists_with_id(user_id=user_id):
            raise UserNotFoundError(field=User.id.name)

        errors = get_user_data_errors(user_data=user_data, check_missing_data=False)
        if len(errors):
            raise UserNotValidError(errors=errors)

        first_name: Optional[str] = user_data.get('first_name')
        last_name: Optional[str] = user_data.get('last_name')
        username: Optional[str] = user_data.get('username')
        email: Optional[str] = user_data.get('email')
        password: Optional[str] = user_data.get('password')
        password_hash: Optional[str] = None

        if password:
            password_hash = hash_password(password=password)

        exist_field_names = list()
        if username and cls.exists_with_username(username=username):
            exist_field_names.append(User.username.name)
        if email and cls.exists_with_email(email=email):
            exist_field_names.append(User.email.name)

        if len(exist_field_names):
            raise UserAlreadyExistsError(fields=exist_field_names)

        return UserRepository.update(user_id=user_id, first_name=first_name, last_name=last_name,
                                     username=username, email=email, password_hash=password_hash)

    @classmethod
    def update_user_tokens(cls, user_id: int, access_token_jti: str, refresh_token_jti: str) -> User:
        if not cls.exists_with_id(user_id=user_id):
            raise UserNotFoundError(field=User.id.name)

        return UserRepository.update(user_id=user_id, access_token_jti=access_token_jti,
                                     refresh_token_jti=refresh_token_jti)

    @classmethod
    def delete(cls, user_id: int) -> User:
        if not cls.exists_with_id(user_id=user_id):
            raise UserNotFoundError(field=User.id.name)

        return UserRepository.delete(user_id=user_id)

    @classmethod
    def exists_with_id(cls, user_id: int) -> bool:
        return UserRepository.exists_with_id(user_id=user_id)

    @classmethod
    def exists_with_username(cls, username: str) -> bool:
        return UserRepository.exists_with_username(username=username)

    @classmethod
    def exists_with_email(cls, email: str) -> bool:
        return UserRepository.exists_with_email(email=email)