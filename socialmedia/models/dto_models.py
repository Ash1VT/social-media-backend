from dataclasses import dataclass
from datetime import datetime

__all__ = ['UserDto', 'PostDto', 'CommentDto']


@dataclass
class UserDto:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    registered_at: datetime
    posts_count: int


@dataclass
class PostDto:
    id: int
    title: str
    body: str
    created_at: datetime
    updated_at: datetime
    likes_count: int
    dislikes_count: int
    user: UserDto


@dataclass
class CommentDto:
    id: int
    text: str
    created_at: datetime
    updated_at: datetime
    likes_count: int
    dislikes_count: int
    answers_count: int
    user: UserDto
    comment_id: int
    post_id: int
