from typing import Dict, List

from socialmedia.constants import DEFAULT_SUCCESS_RESPONSE, DEFAULT_ERROR_RESPONSE, COMMENT_NOT_FOUND_ERROR_STRING, \
    COMMENT_NOT_DISLIKED_ERROR_STRING, COMMENT_NOT_LIKED_ERROR_STRING, COMMENT_ALREADY_LIKED_ERROR_STRING, \
    COMMENT_ALREADY_DISLIKED_ERROR_STRING, COMMENT_NOT_VALID_ERROR_STRING, \
    USER_REQUESTING_FOREIGN_COMMENT_ID_ERROR_STRING
from socialmedia.models.dto_models import CommentDto


def get_comment_response_body(comment: CommentDto) -> Dict:
    return {
        'id': comment.id,
        'text': comment.text,
        'created_at': comment.created_at,
        'updated_at': comment.updated_at,
        'likes_count': comment.likes_count,
        'dislikes_count': comment.dislikes_count,
        'answers_count': comment.answers_count,
        'user': {
            'id': comment.user.id,
            'first_name': comment.user.first_name,
            'last_name': comment.user.last_name,
            'username': comment.user.username,
            'email': comment.user.email
        },
        'post_id': comment.post_id,
    }


def get_all_comments_response_body(comments: List[CommentDto]) -> List:
    return [
        get_comment_response_body(comment=comment) for comment in comments
    ]


def get_comment_answers_response_body(answers: List[CommentDto]) -> List:
    return [
        get_comment_response_body(comment=answer) for answer in answers
    ]


def get_user_comments_response_body(comments: List[CommentDto]) -> List:
    return [
        get_comment_response_body(comment=comment) for comment in comments
    ]


def get_post_comments_response_body(comments: List[CommentDto]) -> List:
    return [
        get_comment_response_body(comment=comment) for comment in comments
    ]


def get_user_liked_comments_response_body(comments: List[CommentDto]) -> Dict:
    return [
        get_comment_response_body(comment=comment) for comment in comments
    ]


def get_user_disliked_comments_response_body(comments: List[CommentDto]) -> Dict:
    return [
        get_comment_response_body(comment=comment) for comment in comments
    ]


def get_add_comment_response_body(comment: CommentDto) -> Dict:
    return get_comment_response_body(comment=comment)


def get_add_comment_answer_response_body(comment: CommentDto) -> Dict:
    return get_comment_response_body(comment=comment)


def get_like_comment_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_remove_like_comment_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_dislike_comment_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_remove_dislike_comment_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_update_comment_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_patch_comment_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_delete_comment_response_body() -> Dict:
    return DEFAULT_SUCCESS_RESPONSE


def get_comment_not_found_response_body(field: str) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': COMMENT_NOT_FOUND_ERROR_STRING,
        'fields': [field]
    }


def get_comment_not_valid_response_body(errors: Dict[str, List[str]]) -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': COMMENT_NOT_VALID_ERROR_STRING,
        'fields': list(errors.keys()),
        'errors': errors
    }


def get_user_requesting_foreign_comment_id_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': USER_REQUESTING_FOREIGN_COMMENT_ID_ERROR_STRING
    }


def get_comment_already_liked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': COMMENT_ALREADY_LIKED_ERROR_STRING
    }


def get_comment_not_liked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': COMMENT_NOT_LIKED_ERROR_STRING
    }


def get_comment_already_disliked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': COMMENT_ALREADY_DISLIKED_ERROR_STRING
    }


def get_comment_not_disliked_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': COMMENT_NOT_DISLIKED_ERROR_STRING
    }
