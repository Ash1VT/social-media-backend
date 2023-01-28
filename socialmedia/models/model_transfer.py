from abc import ABC, abstractmethod

from socialmedia.models import User, Post, Comment
from socialmedia.models.dto_models import UserDto, PostDto, CommentDto
from setup.database import db

__all__ = ['UserModelTransfer', 'PostModelTransfer', 'CommentModelTransfer']


class ModelTransfer(ABC):

    @staticmethod
    @abstractmethod
    def to_dto_model(database_model: db.Model):
        pass


class UserModelTransfer(ModelTransfer):

    @staticmethod
    def to_dto_model(database_model: User) -> UserDto:
        return UserDto(id=database_model.id, first_name=database_model.first_name,
                       last_name=database_model.last_name, username=database_model.username,
                       email=database_model.email, registered_at=database_model.registered_at,
                       posts_count=database_model.posts.count())


class PostModelTransfer(ModelTransfer):

    @staticmethod
    def to_dto_model(database_model: Post) -> PostDto:
        return PostDto(id=database_model.id, body=database_model.body,
                       title=database_model.title, created_at=database_model.created_at,
                       updated_at=database_model.updated_at,
                       likes_count=database_model.liked_users.count(),
                       dislikes_count=database_model.disliked_users.count(),
                       user=UserModelTransfer.to_dto_model(database_model=database_model.user))


class CommentModelTransfer(ModelTransfer):

    @staticmethod
    def to_dto_model(database_model: Comment) -> CommentDto:
        return CommentDto(id=database_model.id, text=database_model.text,
                          created_at=database_model.created_at,
                          updated_at=database_model.updated_at,
                          likes_count=database_model.liked_users.count(),
                          dislikes_count=database_model.disliked_users.count(),
                          answers_count=database_model.comment_answers.count(),
                          user=UserModelTransfer.to_dto_model(database_model=database_model.user),
                          comment_id=database_model.comment_id,
                          post_id=database_model.post_id
                          )
