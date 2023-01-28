from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from socialmedia.api.services import UserService, PostService, CommentService
from socialmedia.api.blueprints import user_blueprint
from socialmedia.utils import check_request_content_type, check_user_operation_permission_on_user
from socialmedia.responses import get_user_response, get_all_users_response, get_current_user_response, \
    get_update_user_response, get_user_comments_response, \
    get_patch_user_response, get_delete_user_response, get_user_posts_response, get_user_liked_posts_response, \
    get_user_liked_comments_response, get_user_disliked_posts_response, get_user_disliked_comments_response
from socialmedia.decorators import handle_app_errors
from socialmedia.models.model_transfer import PostModelTransfer, UserModelTransfer, CommentModelTransfer

__all__ = []


@user_blueprint.route('/<int:user_id>', methods=['GET'])
@handle_app_errors
def get_user(user_id: int):
    user = UserService.get_by_id(user_id=user_id)
    user_dto = UserModelTransfer.to_dto_model(database_model=user)
    return get_user_response(user=user_dto)


@user_blueprint.route('', methods=['GET'])
@handle_app_errors
def get_all_users():
    users = UserService.get_all()
    users_dto = [UserModelTransfer.to_dto_model(database_model=user) for user in users]
    return get_all_users_response(users=users_dto)


@user_blueprint.route('/current', methods=['GET'])
@handle_app_errors
@jwt_required()
def get_current_user():
    token_sub: dict = get_jwt_identity()
    user_id = token_sub.get('id')

    user = UserService.get_by_id(user_id=user_id)
    user_dto = UserModelTransfer.to_dto_model(database_model=user)
    return get_current_user_response(user=user_dto)


@user_blueprint.route('/<int:user_id>', methods=['PUT'])
@handle_app_errors
@jwt_required()
def update_user(user_id: int):
    request_body = check_request_content_type(request=request)
    check_user_operation_permission_on_user(user_id=user_id, token_identity=get_jwt_identity())
    UserService.update(user_id=user_id, user_data=request_body)

    return get_update_user_response()


@user_blueprint.route('/<int:user_id>', methods=['PATCH'])
@handle_app_errors
@jwt_required()
def patch_user(user_id: int):
    request_body = check_request_content_type(request=request)
    check_user_operation_permission_on_user(user_id=user_id, token_identity=get_jwt_identity())
    UserService.patch(user_id=user_id, user_data=request_body)

    return get_patch_user_response()


@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
@handle_app_errors
@jwt_required()
def delete_user(user_id: int):
    check_user_operation_permission_on_user(user_id=user_id, token_identity=get_jwt_identity())
    UserService.delete(user_id=user_id)
    return get_delete_user_response()


@user_blueprint.route('/<int:user_id>/posts', methods=['GET'])
@handle_app_errors
def get_user_posts(user_id: int):
    posts = PostService.get_user_posts(user_id=user_id)
    posts_dto = [PostModelTransfer.to_dto_model(database_model=post) for post in posts]
    return get_user_posts_response(posts=posts_dto)


@user_blueprint.route('/<int:user_id>/comments', methods=['GET'])
@handle_app_errors
def get_user_comments(user_id: int):
    comments = CommentService.get_user_comments(user_id=user_id)
    comments_dto = [CommentModelTransfer.to_dto_model(database_model=comment) for comment in comments]
    return get_user_comments_response(comments=comments_dto)


@user_blueprint.route('/<int:user_id>/posts/liked', methods=['GET'])
@handle_app_errors
def get_liked_posts(user_id: int):
    posts = PostService.get_user_liked_posts(user_id=user_id)
    posts_dto = [PostModelTransfer.to_dto_model(database_model=post) for post in posts]
    return get_user_liked_posts_response(posts=posts_dto)


@user_blueprint.route('/<int:user_id>/posts/disliked', methods=['GET'])
@handle_app_errors
def get_disliked_posts(user_id: int):
    posts = PostService.get_user_liked_posts(user_id=user_id)
    posts_dto = [PostModelTransfer.to_dto_model(database_model=post) for post in posts]
    return get_user_disliked_posts_response(posts=posts_dto)


@user_blueprint.route('/<int:user_id>/comments/liked', methods=['GET'])
@handle_app_errors
def get_liked_comments(user_id: int):
    comments = CommentService.get_user_liked_comments(user_id=user_id)
    comments_dto = [CommentModelTransfer.to_dto_model(database_model=comment) for comment in comments]
    return get_user_liked_comments_response(comments=comments_dto)


@user_blueprint.route('/<int:user_id>/comments/disliked', methods=['GET'])
@handle_app_errors
def get_disliked_comments(user_id: int):
    comments = CommentService.get_user_disliked_comments(user_id=user_id)
    comments_dto = [CommentModelTransfer.to_dto_model(database_model=comment) for comment in comments]
    return get_user_disliked_comments_response(comments=comments_dto)
