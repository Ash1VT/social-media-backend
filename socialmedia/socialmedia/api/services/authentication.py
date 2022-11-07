from typing import Optional

from socialmedia.socialmedia.db import User
from socialmedia.socialmedia.api.repositories import UserRepository
from .security import check_password


def authenticate(username: str, password: str) -> Optional[User]:
    user = UserRepository.get_by_username(username=username)
    if not user:
        return

    user_password = user.password_hash
    if check_password(password=password, hashed_password=user_password):
        return user
