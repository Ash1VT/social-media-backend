from datetime import datetime
from typing import List, Optional

from setup import db
from .base import BaseRepository

__all__ = ['PostRepository']

from ...models import Post, User


class PostRepository(BaseRepository):

    @classmethod
    def get_all(cls) -> List[Post]:
        return Post.query.all()

    @classmethod
    def get_user_posts(cls, user_id: int) -> List[Post]:
        return User.query.filter_by(id=user_id).first().posts.all()

    @classmethod
    def get_user_liked_posts(cls, user_id: int) -> List[Post]:
        return User.query.filter_by(id=user_id).first().liked_posts.all()

    @classmethod
    def get_user_disliked_posts(cls, user_id: int) -> List[Post]:
        return User.query.filter_by(id=user_id).first().disliked_posts.all()

    @classmethod
    def get_by_id(cls, post_id: int) -> Optional[Post]:
        return Post.query.filter_by(id=post_id).first()

    @classmethod
    def add(cls, title: str, body: str, user_id: int) -> Post:
        post = Post(title=title, body=body, user_id=user_id)
        db.session.add(post)
        cls.commit()
        return post

    @classmethod
    def update(cls, post_id: int, updated_at: datetime, title: str = None, body: str = None) -> Post:
        post = cls.get_by_id(post_id=post_id)
        if title:
            post.title = title
        if body:
            post.body = body
        post.updated_at = updated_at
        cls.commit()
        return post

    @classmethod
    def delete(cls, post_id: int) -> Post:
        post = cls.get_by_id(post_id=post_id)
        db.session.delete(post)
        cls.commit()
        return post

    @classmethod
    def exists_with_id(cls, post_id: int) -> bool:
        return db.session.query(Post.query.filter_by(id=post_id).exists()).scalar()
