from typing import Tuple, Dict, List

from flask import jsonify, Response

from socialmedia.models.dto_models import PostDto
from socialmedia.responses.body import get_post_response_body, get_all_posts_response_body, \
    get_user_posts_response_body, get_user_liked_posts_response_body, get_add_post_response_body, \
    get_like_post_response_body, get_remove_like_post_response_body, \
    get_update_post_response_body, get_patch_post_response_body, get_delete_post_response_body, \
    get_post_not_found_response_body, get_post_not_valid_response_body, \
    get_user_requesting_foreign_post_id_response_body, \
    get_post_already_liked_response_body, get_post_not_liked_response_body, \
    get_dislike_post_response_body, get_remove_dislike_post_response_body, \
    get_post_already_disliked_response_body, get_post_not_disliked_response_body


def get_post_response(post: PostDto) -> Tuple[Response, int]:
    return jsonify(get_post_response_body(post=post)), 200


def get_all_posts_response(posts: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_all_posts_response_body(posts=posts)), 200


def get_user_posts_response(posts: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_user_posts_response_body(posts=posts)), 200


def get_user_liked_posts_response(posts: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_user_liked_posts_response_body(posts=posts)), 200


def get_user_disliked_posts_response(posts: List[PostDto]) -> Tuple[Response, int]:
    return jsonify(get_user_liked_posts_response_body(posts=posts)), 200


def get_add_post_response(post: PostDto) -> Tuple[Response, int]:
    return jsonify(get_add_post_response_body(post=post)), 200


def get_like_post_response() -> Tuple[Response, int]:
    return jsonify(get_like_post_response_body()), 200


def get_remove_like_post_response() -> Tuple[Response, int]:
    return jsonify(get_remove_like_post_response_body()), 200


def get_dislike_post_response() -> Tuple[Response, int]:
    return jsonify(get_dislike_post_response_body()), 200


def get_remove_dislike_post_response() -> Tuple[Response, int]:
    return jsonify(get_remove_dislike_post_response_body()), 200


def get_update_post_response() -> Tuple[Response, int]:
    return jsonify(get_update_post_response_body()), 200


def get_patch_post_response() -> Tuple[Response, int]:
    return jsonify(get_patch_post_response_body()), 200


def get_delete_post_response() -> Tuple[Response, int]:
    return jsonify(get_delete_post_response_body()), 200


def get_post_not_found_response(field: str) -> Tuple[Response, int]:
    return jsonify(get_post_not_found_response_body(field=field)), 400


def get_post_not_valid_response(errors: Dict[str, List[str]]) -> Tuple[Response, int]:
    return jsonify(get_post_not_valid_response_body(errors=errors)), 400


def get_user_requesting_foreign_post_id_response() -> Tuple[Response, int]:
    return jsonify(get_user_requesting_foreign_post_id_response_body()), 403


def get_post_already_liked_response() -> Tuple[Response, int]:
    return jsonify(get_post_already_liked_response_body()), 403


def get_post_not_liked_response() -> Tuple[Response, int]:
    return jsonify(get_post_not_liked_response_body()), 403


def get_post_already_disliked_response() -> Tuple[Response, int]:
    return jsonify(get_post_already_disliked_response_body()), 403


def get_post_not_disliked_response() -> Tuple[Response, int]:
    return jsonify(get_post_not_disliked_response_body()), 403
