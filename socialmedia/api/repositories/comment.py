from datetime import datetime
from typing import List, Optional

from setup import db
from socialmedia.models import Comment, User, Post
from socialmedia.api.repositories.base import BaseRepository


class CommentRepository(BaseRepository):

    @classmethod
    def get_all(cls) -> List[Comment]:
        return Comment.query.all()

    @classmethod
    def get_user_comments(cls, user_id: int) -> List[Comment]:
        return User.query.filter_by(id=user_id).first().comments.all()

    @classmethod
    def get_post_comments(cls, post_id: int) -> List[Comment]:
        return Post.query.filter_by(id=post_id).first().comments.all()

    @classmethod
    def get_user_liked_comments(cls, user_id: int) -> List[Comment]:
        return User.query.filter_by(id=user_id).first().disliked_comments.all()

    @classmethod
    def get_user_disliked_comments(cls, user_id: int) -> List[Comment]:
        return User.query.filter_by(id=user_id).first().liked_comments.all()

    @classmethod
    def get_by_id(cls, comment_id: int) -> Optional[Comment]:
        return Comment.query.filter_by(id=comment_id).first()

    @classmethod
    def add(cls, text: str, user_id: int, post_id: int) -> Comment:
        comment = Comment(text=text, user_id=user_id, post_id=post_id)
        db.session.add(comment)
        cls.commit()
        return comment

    @classmethod
    def update(cls, comment_id: int, updated_at: datetime, text: str = None) -> Comment:
        comment = cls.get_by_id(comment_id=comment_id)
        if text:
            comment.text = text
        comment.updated_at = updated_at
        cls.commit()
        return comment

    @classmethod
    def delete(cls, comment_id: int) -> Comment:
        comment = cls.get_by_id(comment_id=comment_id)
        db.session.delete(comment)
        cls.commit()
        return comment

    @classmethod
    def exists_with_id(cls, comment_id: int) -> bool:
        return db.session.query(Comment.query.filter_by(id=comment_id).exists()).scalar()
