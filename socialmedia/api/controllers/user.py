from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from socialmedia.api.services import UserService
from socialmedia.api.blueprints import user_blueprint
from socialmedia.utils import check_request_content_type, get_requesting_id, verify_id_in_token_identity
from socialmedia.responses import get_user_response, get_all_users_response, get_current_user_response, get_update_user_response, \
    get_patch_user_response, get_delete_user_response
from socialmedia.decorators import handle_app_errors

__all__ = []


@user_blueprint.route('/<id>', methods=['GET'])
@handle_app_errors
def get_user(id: str):
    user_id = get_requesting_id(user_id=id)
    user = UserService.get_by_id(user_id=user_id)

    return get_user_response(user=user)


@user_blueprint.route('', methods=['GET'])
@handle_app_errors
def get_all_users():
    users = UserService.get_all()
    return get_all_users_response(users=users)


@user_blueprint.route('/current', methods=['GET'])
@handle_app_errors
@jwt_required()
def get_current_user():
    token_sub: dict = get_jwt_identity()
    user_id = token_sub.get('id')

    user = UserService.get_by_id(user_id=user_id)

    return get_current_user_response(user=user)


@user_blueprint.route('/<id>', methods=['PUT'])
@handle_app_errors
@jwt_required()
def update_user(id: str):
    request_body = check_request_content_type(request=request)
    user_id = verify_id_in_token_identity(user_id=id, token_identity=get_jwt_identity())
    UserService.update(user_id=user_id, user_data=request_body)

    return get_update_user_response()


@user_blueprint.route('/<id>', methods=['PATCH'])
@handle_app_errors
@jwt_required()
def patch_user(id: str):
    request_body = check_request_content_type(request=request)
    user_id = verify_id_in_token_identity(user_id=id, token_identity=get_jwt_identity())
    UserService.patch(user_id=user_id, user_data=request_body)

    return get_patch_user_response()


@user_blueprint.route('/<id>', methods=['DELETE'])
@handle_app_errors
@jwt_required()
def delete_user(id: str):
    user_id = verify_id_in_token_identity(user_id=id, token_identity=get_jwt_identity())
    UserService.delete(user_id=user_id)

    return get_delete_user_response()
