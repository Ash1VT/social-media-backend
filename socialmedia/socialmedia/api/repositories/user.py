from typing import Optional, List

from sqlalchemy import or_

from socialmedia.socialmedia.models import User
from setup import db
from .base import BaseRepository


class UserRepository(BaseRepository):

    @classmethod
    def get_all(cls) -> List[User]:
        return User.query.all()

    @classmethod
    def get_by_username(cls, username: str) -> Optional[User]:
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_id(cls, id: int) -> Optional[User]:
        return User.query.filter_by(id=id).first()

    @classmethod
    def append(cls, user: User):
        db.session.add(user)
        cls.commit()

    @classmethod
    def update(cls, user: User, first_name=None, last_name=None, username=None, email=None, password_hash=None,
               refresh_token_jti=None):
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if username:
            user.username = username
        if email:
            user.email = email
        if password_hash:
            user.password_hash = password_hash
        if refresh_token_jti:
            user.refresh_token_jti = refresh_token_jti
        cls.commit()

    @classmethod
    def exists(cls, first_name=None, last_name=None, username=None, email=None, password_hash=None, refresh_token_jti=None):
        users = User.query.filter(
            (User.first_name == first_name) |
            (User.last_name == last_name) |
            (User.username == username) |
            (User.email == email) |
            (User.password_hash == password_hash) |
            (User.refresh_token_jti == refresh_token_jti)
        ).all()

        non_unique = list()
        if first_name and len([user for user in users if user.first_name == first_name]):
            non_unique.append(User.first_name.name)
        if last_name and len([user for user in users if user.last_name == last_name]):
            non_unique.append(User.last_name.name)
        if username and len([user for user in users if user.username == username]):
            non_unique.append(User.username.name)
        if email and len([user for user in users if user.email == email]):
            non_unique.append(User.email.name)
        if password_hash and len([user for user in users if user.password_hash == password_hash]):
            non_unique.append(User.password_hash.name)
        if refresh_token_jti and len([user for user in users if user.refresh_token_jti == refresh_token_jti]):
            non_unique.append(User.refresh_token_jti.name)
        return non_unique
