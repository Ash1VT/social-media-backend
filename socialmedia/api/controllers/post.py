from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from socialmedia.api.blueprints import post_blueprint
from socialmedia.api.services import PostService, CommentService
from socialmedia.decorators import handle_app_errors
from socialmedia.responses import get_post_response, get_all_posts_response, get_like_post_response, \
    get_remove_like_post_response, get_add_comment_response, \
    get_add_post_response, get_delete_post_response, get_dislike_post_response, get_remove_dislike_post_response, \
    get_post_comments_response, get_update_post_response, get_patch_post_response
from socialmedia.utils import check_request_content_type, \
    check_user_operation_permission_on_post, get_user_id
from socialmedia.models.model_transfer import PostModelTransfer, CommentModelTransfer


@post_blueprint.route('/<int:post_id>', methods=['GET'])
@handle_app_errors
def get_post(post_id: int):
    post = PostService.get_by_id(post_id=post_id)
    post_dto = PostModelTransfer.to_dto_model(database_model=post)
    return get_post_response(post=post_dto)


@post_blueprint.route('', methods=['GET'])
@handle_app_errors
def get_all_posts():
    posts = PostService.get_all()
    posts_dto = [PostModelTransfer.to_dto_model(database_model=post) for post in posts]
    return get_all_posts_response(posts=posts_dto)


@post_blueprint.route('/<int:post_id>/comments', methods=['GET'])
@handle_app_errors
def get_post_comments(post_id: int):
    comments = CommentService.get_post_comments(post_id=post_id)
    comments_dto = [CommentModelTransfer.to_dto_model(database_model=comment) for comment in comments]
    return get_post_comments_response(comments=comments_dto)


@post_blueprint.route('', methods=['POST'])
@handle_app_errors
@jwt_required()
def add_post():
    request_body: dict = check_request_content_type(request=request)
    user_id = int(get_jwt_identity().get('id'))

    request_body['user_id'] = user_id

    post = PostService.add(post_data=request_body)
    post_dto = PostModelTransfer.to_dto_model(database_model=post)
    return get_add_post_response(post=post_dto)


@post_blueprint.route('/<int:post_id>/comment', methods=['POST'])
@handle_app_errors
@jwt_required()
def add_post_comment(post_id: int):
    request_body: dict = check_request_content_type(request=request)
    user_id = int(get_jwt_identity().get('id'))

    request_body['user_id'] = user_id
    request_body['post_id'] = post_id

    comment = CommentService.add(comment_data=request_body)
    comment_dto = CommentModelTransfer.to_dto_model(database_model=comment)
    return get_add_comment_response(comment=comment_dto)


@post_blueprint.route('/<int:post_id>/like', methods=['POST'])
@handle_app_errors
@jwt_required()
def like_post(post_id: int):
    user_id: int = get_user_id(token_identity=get_jwt_identity())
    PostService.like_post(user_id=user_id, post_id=post_id)
    return get_like_post_response()


@post_blueprint.route('/<int:post_id>/like', methods=['DELETE'])
@handle_app_errors
@jwt_required()
def remove_like_post(post_id: int):
    user_id: int = get_user_id(token_identity=get_jwt_identity())
    PostService.remove_like_post(user_id=user_id, post_id=post_id)
    return get_remove_like_post_response()


@post_blueprint.route('/<int:post_id>/dislike', methods=['POST'])
@handle_app_errors
@jwt_required()
def dislike_post(post_id: int):
    user_id: int = get_user_id(token_identity=get_jwt_identity())
    PostService.dislike_post(user_id=user_id, post_id=post_id)
    return get_dislike_post_response()


@post_blueprint.route('/<int:post_id>/dislike', methods=['DELETE'])
@handle_app_errors
@jwt_required()
def remove_dislike_post(post_id: int):
    user_id: int = get_user_id(token_identity=get_jwt_identity())
    PostService.remove_dislike_post(user_id=user_id, post_id=post_id)
    return get_remove_dislike_post_response()


@post_blueprint.route('/<int:post_id>', methods=['PUT'])
@handle_app_errors
@jwt_required()
def update_post(post_id: int):
    request_body = check_request_content_type(request=request)

    post = PostService.get_by_id(post_id=post_id)

    post_author_id: int = post.user_id

    check_user_operation_permission_on_post(post_author_id=post_author_id, token_identity=get_jwt_identity())
    PostService.update(post_id=post_id, post_data=request_body)

    return get_update_post_response()


@post_blueprint.route('/<int:post_id>', methods=['PATCH'])
@handle_app_errors
@jwt_required()
def patch_post(post_id: int):
    request_body = check_request_content_type(request=request)

    post = PostService.get_by_id(post_id=post_id)

    post_author_id: int = post.user_id

    check_user_operation_permission_on_post(post_author_id=post_author_id, token_identity=get_jwt_identity())
    PostService.patch(post_id=post_id, post_data=request_body)

    return get_patch_post_response()


@post_blueprint.route('/<int:post_id>', methods=['DELETE'])
@handle_app_errors
@jwt_required()
def delete_post(post_id: int):
    post = PostService.get_by_id(post_id=post_id)

    post_author_id: int = post.user_id

    check_user_operation_permission_on_post(post_author_id=post_author_id, token_identity=get_jwt_identity())

    PostService.delete(post_id=post_id)
    return get_delete_post_response()
