from typing import List, Optional
from datetime import datetime

from socialmedia.errors import UserNotFoundError, PostNotFoundError, PostNotValidError, PostAlreadyLikedError, \
    PostNotLikedError, PostAlreadyDislikedError, PostNotDislikedError
from socialmedia.models import Post, User
from socialmedia.utils import get_post_data_errors
from socialmedia.api.repositories import PostRepository

from .user import UserService

__all__ = ['PostService']


class PostService:

    @classmethod
    def get_all(cls) -> List[Post]:
        return PostRepository.get_all()

    @classmethod
    def get_by_id(cls, post_id: int) -> Post:
        post = PostRepository.get_by_id(post_id=post_id)

        if not post:
            raise PostNotFoundError(field=Post.id.name)

        return post

    @classmethod
    def get_user_posts(cls, user_id: int) -> List[Post]:
        user = UserService.get_by_id(user_id=user_id)
        return user.posts

    @classmethod
    def get_user_liked_posts(cls, user_id: int) -> List[Post]:
        user = UserService.get_by_id(user_id=user_id)
        return user.liked_posts

    @classmethod
    def get_user_disliked_posts(cls, user_id: int) -> List[Post]:
        user = UserService.get_by_id(user_id=user_id)
        return user.disliked_posts

    @classmethod
    def add(cls, post_data: dict) -> Post:
        errors = get_post_data_errors(post_data=post_data, check_missing_data=True)

        if len(errors):
            raise PostNotValidError(errors=errors)

        title: str = post_data.get('title')
        body: str = post_data.get('body')
        user_id: int = int(post_data.get('user_id'))

        if not UserService.exists_with_id(user_id=user_id):
            raise UserNotFoundError(field=User.id.name)

        return PostRepository.add(title=title, body=body, user_id=user_id)

    @classmethod
    def like_post(cls, user_id: int, post_id: int) -> None:
        post = cls.get_by_id(post_id=post_id)
        user = UserService.get_by_id(user_id=user_id)

        if user in post.liked_users:
            raise PostAlreadyLikedError()

        if user in post.disliked_users:
            cls.remove_dislike_post(user_id=user_id, post_id=post_id)

        post.liked_users.append(user)
        PostRepository.commit()

    @classmethod
    def remove_like_post(cls, user_id: int, post_id: int) -> None:
        post = cls.get_by_id(post_id=post_id)
        user = UserService.get_by_id(user_id=user_id)

        if user not in post.liked_users:
            raise PostNotLikedError()

        post.liked_users.remove(user)
        PostRepository.commit()

    @classmethod
    def dislike_post(cls, user_id: int, post_id: int) -> None:
        post = cls.get_by_id(post_id=post_id)
        user = UserService.get_by_id(user_id=user_id)

        if user in post.disliked_users:
            raise PostAlreadyDislikedError()

        if user in post.liked_users:
            cls.remove_like_post(user_id=user_id, post_id=post_id)

        post.disliked_users.append(user)
        PostRepository.commit()

    @classmethod
    def remove_dislike_post(cls, user_id: int, post_id: int) -> None:
        post = cls.get_by_id(post_id=post_id)
        user = UserService.get_by_id(user_id=user_id)

        if user not in post.disliked_users:
            raise PostNotDislikedError()

        post.disliked_users.remove(user)
        PostRepository.commit()

    @classmethod
    def update(cls, post_id: int, post_data: dict) -> Post:
        if not cls.exists_with_id(post_id=post_id):
            raise PostNotFoundError(field=Post.id.name)

        errors = get_post_data_errors(post_data=post_data, check_missing_data=True)
        if len(errors):
            raise PostNotValidError(errors=errors)

        title: str = post_data.get('title')
        body: str = post_data.get('body')
        updated_at: datetime = datetime.utcnow()

        return PostRepository.update(post_id=post_id, title=title, body=body, updated_at=updated_at)

    @classmethod
    def patch(cls, post_id: int, post_data: dict) -> User:
        if not cls.exists_with_id(post_id=post_id):
            raise PostNotFoundError(field=Post.id.name)

        errors = get_post_data_errors(post_data=post_data, check_missing_data=False)
        if len(errors):
            raise PostNotValidError(errors=errors)

        title: Optional[str] = post_data.get('title')
        body: Optional[str] = post_data.get('body')
        updated_at: datetime = datetime.utcnow()

        return PostRepository.update(post_id=post_id, title=title, body=body, updated_at=updated_at)

    @classmethod
    def delete(cls, post_id: int) -> Post:
        if not cls.exists_with_id(post_id=post_id):
            raise PostNotFoundError(field=Post.id.name)

        return PostRepository.delete(post_id=post_id)

    @classmethod
    def exists_with_id(cls, post_id: int) -> bool:
        return PostRepository.exists_with_id(post_id=post_id)
