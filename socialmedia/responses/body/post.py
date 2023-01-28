from typing import Dict, List

from socialmedia.models.dto_models import PostDto
from socialmedia.constants import DEFAULT_SUCCESS_RESPONSE, DEFAULT_ERROR_RESPONSE, POST_NOT_FOUND_ERROR_STRING, \
    POST_NOT_VALID_ERROR_STRING, USER_REQUESTING_FOREIGN_POST_ID_ERROR_STRING, \
    POST_ALREADY_LIKED_ERROR_STRING, POST_NOT_LIKED_ERROR_STRING, POST_ALREADY_DISLIKED_ERROR_STRING, \
    POST_NOT_DISLIKED_ERROR_STRING


def get_post_response_body(post: PostDto) -> Dict:
    return {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'created_at': post.created_at,
            'updated_at': post.updated_at,
            'likes_count': post.likes_count,
            'dislikes_count': post.dislikes_count,
            'user': {
                'id': post.user.id,
                'first_name': post.user.first_name,
                'last_name': post.user.last_name,
                'username': post.user.username,
                'email': post.user.email,
                }
            }


def get_all_posts_response_body(posts: List[PostDto]) -> List:
    return [
        get_post_response_body(post=post) for post in posts
    ]


def get_user_posts_response_body(posts: List[PostDto]) -> List:
    return [
        get_post_response_body(post=post) for post in posts
    ]


def get_user_liked_posts_response_body(posts: List[PostDto]) -> Dict:
    return [
        get_post_response_body(post=post) for post in posts
    ]


def get_user_disliked_posts_response_body(posts: List[PostDto]) -> Dict:
    return [
        get_post_response_body(post=post) for post in posts
    ]


def get_add_post_response_body(post: PostDto) -> Dict:
    return get_post_response_body(post=post)


def get_like_post_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_remove_like_post_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_dislike_post_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_remove_dislike_post_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_update_post_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_patch_post_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_delete_post_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_post_not_found_response_body(field: str) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': POST_NOT_FOUND_ERROR_STRING,
        'fields': [field]
    }


def get_post_not_valid_response_body(errors: Dict[str, List[str]]) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': POST_NOT_VALID_ERROR_STRING,
        'fields': list(errors.keys()),
        'errors': errors
    }


def get_user_requesting_foreign_post_id_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': USER_REQUESTING_FOREIGN_POST_ID_ERROR_STRING
    }


def get_post_already_liked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': POST_ALREADY_LIKED_ERROR_STRING
    }


def get_post_not_liked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': POST_NOT_LIKED_ERROR_STRING
    }


def get_post_already_disliked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': POST_ALREADY_DISLIKED_ERROR_STRING
    }


def get_post_not_disliked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': POST_NOT_DISLIKED_ERROR_STRING
    }
