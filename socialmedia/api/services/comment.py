from typing import List, Optional

from socialmedia.api.services import UserService, PostService
from socialmedia.models import Comment, User, Post
from socialmedia.api.repositories import CommentRepository
from socialmedia.errors import CommentNotFoundError, CommentNotValidError, CommentNotDislikedError, \
    CommentAlreadyDislikedError, CommentAlreadyLikedError, CommentNotLikedError, UserNotFoundError, PostNotFoundError
from socialmedia.utils import get_comment_data_errors

__all__ = ['CommentService']


class CommentService:

    @classmethod
    def get_all(cls) -> List[Comment]:
        return CommentRepository.get_all()

    @classmethod
    def get_by_id(cls, comment_id: int) -> Comment:
        comment = CommentRepository.get_by_id(comment_id=comment_id)

        if not comment:
            raise CommentNotFoundError(field=Comment.id.name)

        return comment

    @classmethod
    def get_user_comments(cls, user_id: int) -> List[Comment]:
        return CommentRepository.get_user_comments(user_id=user_id)

    @classmethod
    def get_post_comments(cls, post_id: int) -> List[Comment]:
        return CommentRepository.get_post_comments(post_id=post_id)

    @classmethod
    def get_user_liked_comments(cls, user_id: int) -> List[Comment]:
        user = UserService.get_by_id(user_id=user_id)
        return user.liked_comments

    @classmethod
    def get_user_disliked_comments(cls, user_id: int) -> List[Comment]:
        user = UserService.get_by_id(user_id=user_id)
        return user.disliked_comments

    @classmethod
    def add(cls, comment_data: dict) -> Comment:
        errors = get_comment_data_errors(comment_data=comment_data, check_missing_data=True)

        if len(errors):
            raise CommentNotValidError(errors=errors)

        text: str = comment_data.get('text')
        user_id: int = int(comment_data.get('user_id'))
        post_id: int = int(comment_data.get('post_id'))

        if not UserService.exists_with_id(user_id=user_id):
            raise UserNotFoundError(field=User.id.name)

        if not PostService.exists_with_id(post_id=post_id):
            raise PostNotFoundError(field=Post.id.name)

        return CommentRepository.add(text=text, user_id=user_id, post_id=post_id)

    @classmethod
    def add_comment_answer(cls, comment_id: int, answer_comment_data: dict) -> Comment:
        comment = cls.add(comment_data=answer_comment_data)
        comment.comment_id = comment_id
        CommentRepository.commit()
        return comment

    @classmethod
    def like_comment(cls, user_id: int, comment_id: int) -> None:
        comment = cls.get_by_id(comment_id=comment_id)
        user = UserService.get_by_id(user_id=user_id)

        if user in comment.liked_users:
            raise CommentAlreadyLikedError()

        if user in comment.disliked_users:
            cls.remove_dislike_comment(user_id=user_id, comment_id=comment_id)

        comment.liked_users.append(user)
        CommentRepository.commit()

    @classmethod
    def remove_like_comment(cls, user_id: int, comment_id: int) -> None:
        comment = cls.get_by_id(comment_id=comment_id)
        user = UserService.get_by_id(user_id=user_id)

        if user not in comment.liked_users:
            raise CommentNotLikedError()

        comment.liked_users.remove(user)
        CommentRepository.commit()

    @classmethod
    def dislike_comment(cls, user_id: int, comment_id: int) -> None:
        comment = cls.get_by_id(comment_id=comment_id)
        user = UserService.get_by_id(user_id=user_id)

        if user in comment.disliked_users:
            raise CommentAlreadyDislikedError()

        if user in comment.liked_users:
            cls.remove_like_comment(user_id=user_id, comment_id=comment_id)

        comment.disliked_users.append(user)
        CommentRepository.commit()

    @classmethod
    def remove_dislike_comment(cls, user_id: int, comment_id: int) -> None:
        comment = cls.get_by_id(comment_id=comment_id)
        user = UserService.get_by_id(user_id=user_id)

        if user not in comment.disliked_users:
            raise CommentNotDislikedError()

        comment.disliked_users.remove(user)
        CommentRepository.commit()

    @classmethod
    def update(cls, comment_id: int, comment_data: dict) -> Comment:
        if not cls.exists_with_id(comment_id=comment_id):
            raise CommentNotFoundError(field=Comment.id.name)

        errors = get_comment_data_errors(comment_data=comment_data, check_missing_data=True)
        if len(errors):
            raise CommentNotValidError(errors=errors)

        text: str = comment_data.get('text')

        return CommentRepository.update(comment_id=comment_id, text=text)

    @classmethod
    def patch(cls, comment_id: int, comment_data: dict) -> User:
        if not cls.exists_with_id(comment_id=comment_id):
            raise CommentNotFoundError(field=Comment.id.name)

        errors = get_comment_data_errors(comment_data=comment_data, check_missing_data=False)
        if len(errors):
            raise CommentNotValidError(errors=errors)

        text: Optional[str] = comment_data.get('text')

        return CommentRepository.update(comment_id=comment_id, text=text)

    @classmethod
    def delete(cls, comment_id: int) -> Comment:
        if not cls.exists_with_id(comment_id=comment_id):
            raise CommentNotFoundError(field=Comment.id.name)

        return CommentRepository.delete(comment_id=comment_id)

    @classmethod
    def exists_with_id(cls, comment_id: int) -> bool:
        return CommentRepository.exists_with_id(comment_id=comment_id)
