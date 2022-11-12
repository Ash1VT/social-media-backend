from typing import Optional, List

from socialmedia.models import User, UserTokens
from setup import db
from .base import BaseRepository

__all__ = ['UserRepository']


class UserRepository(BaseRepository):

    @classmethod
    def get_all(cls) -> List[User]:
        return User.query.all()

    @classmethod
    def get_by_username(cls, username: str) -> Optional[User]:
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email: str) -> Optional[User]:
        return User.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, user_id: int) -> Optional[User]:
        return User.query.filter_by(id=user_id).first()

    @classmethod
    def add(cls, first_name: str, last_name: str, username: str, email: str, password_hash: str) -> User:
        user_tokens = UserTokens()
        user = User(first_name=first_name, last_name=last_name,
                    username=username, email=email,
                    password_hash=password_hash, user_tokens=user_tokens)
        db.session.add(user)
        cls.commit()
        return user

    @classmethod
    def update(cls, user_id: int, first_name: str = None, last_name: str = None, username: str = None,
               email: str = None, password_hash: str = None, access_token_jti: str = None, refresh_token_jti: str = None) -> User:
        user = cls.get_by_id(user_id=user_id)
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
        if access_token_jti:
            user.user_tokens.access_token_jti = access_token_jti
        if refresh_token_jti:
            user.user_tokens.refresh_token_jti = refresh_token_jti
        cls.commit()
        return user

    @classmethod
    def delete(cls, user_id: int) -> User:
        user = cls.get_by_id(user_id=user_id)
        db.session.delete(user.user_tokens)
        db.session.delete(user)
        cls.commit()
        return user

    @classmethod
    def exists_with_id(cls, user_id: int) -> bool:
        return db.session.query(User.query.filter_by(id=user_id).exists()).scalar()

    @classmethod
    def exists_with_username(cls, username: str) -> bool:
        return db.session.query(User.query.filter_by(username=username).exists()).scalar()

    @classmethod
    def exists_with_email(cls, email: str) -> bool:
        return db.session.query(User.query.filter_by(email=email).exists()).scalar()