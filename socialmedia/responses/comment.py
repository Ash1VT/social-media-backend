from typing import Tuple, List, Dict

from flask import Response, jsonify

from socialmedia.models.dto_models import PostDto
from socialmedia.responses.body.comment import get_comment_response_body, get_all_comments_response_body, \
    get_user_comments_response_body, get_user_liked_comments_response_body, get_add_comment_response_body, \
    get_like_comment_response_body, get_remove_like_comment_response_body, get_dislike_comment_response_body, \
    get_remove_dislike_comment_response_body, get_update_comment_response_body, get_patch_comment_response_body, \
    get_delete_comment_response_body, get_comment_not_found_response_body, get_comment_not_valid_response_body, \
    get_comment_not_disliked_response_body, get_comment_already_disliked_response_body, \
    get_comment_not_liked_response_body, get_comment_already_liked_response_body, \
    get_user_requesting_foreign_comment_id_response_body, get_comment_answers_response_body, \
    get_post_comments_response_body


def get_comment_response(comment: PostDto) -> Tuple[Response, int]:
    return jsonify(get_comment_response_body(comment=comment)), 200


def get_all_comments_response(comments: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_all_comments_response_body(comments=comments)), 200


def get_comment_answers_response(answers: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_comment_answers_response_body(answers=answers)), 200


def get_user_comments_response(comments: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_user_comments_response_body(comments=comments)), 200


def get_post_comments_response(comments: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_post_comments_response_body(comments=comments)), 200


def get_user_liked_comments_response(comments: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_user_liked_comments_response_body(comments=comments)), 200


def get_user_disliked_comments_response(comments: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_user_liked_comments_response_body(comments=comments)), 200


def get_add_comment_response(comment: PostDto) -> Tuple[Response, int]:
    return jsonify(get_add_comment_response_body(comment=comment)), 200


def get_add_comment_answer_response(comment: PostDto) -> Tuple[Response, int]:
    return jsonify(get_add_comment_response_body(comment=comment)), 200


def get_like_comment_response() -> Tuple[Response, int]:
    return jsonify(get_like_comment_response_body()), 200


def get_remove_like_comment_response() -> Tuple[Response, int]:
    return jsonify(get_remove_like_comment_response_body()), 200


def get_dislike_comment_response() -> Tuple[Response, int]:
    return jsonify(get_dislike_comment_response_body()), 200


def get_remove_dislike_comment_response() -> Tuple[Response, int]:
    return jsonify(get_remove_dislike_comment_response_body()), 200


def get_update_comment_response() -> Tuple[Response, int]:
    return jsonify(get_update_comment_response_body()), 200


def get_patch_comment_response() -> Tuple[Response, int]:
    return jsonify(get_patch_comment_response_body()), 200


def get_delete_comment_response() -> Tuple[Response, int]:
    return jsonify(get_delete_comment_response_body()), 200


def get_comment_not_found_response(field: str) -> Tuple[Response, int]:
    return jsonify(get_comment_not_found_response_body(field=field)), 400


def get_comment_not_valid_response(errors: Dict[str, List[str]]) -> Tuple[Response, int]:
    return jsonify(get_comment_not_valid_response_body(errors=errors)), 400


def get_user_requesting_foreign_comment_id_response() -> Tuple[Response, int]:
    return jsonify(get_user_requesting_foreign_comment_id_response_body()), 403


def get_comment_already_liked_response() -> Tuple[Response, int]:
    return jsonify(get_comment_already_liked_response_body()), 403


def get_comment_not_liked_response() -> Tuple[Response, int]:
    return jsonify(get_comment_not_liked_response_body()), 403


def get_comment_already_disliked_response() -> Tuple[Response, int]:
    return jsonify(get_comment_already_disliked_response_body()), 403


def get_comment_not_disliked_response() -> Tuple[Response, int]:
    return jsonify(get_comment_not_disliked_response_body()), 403
