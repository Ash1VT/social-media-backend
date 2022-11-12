from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, set_refresh_cookies, set_access_cookies, \
    unset_jwt_cookies

from socialmedia.api.services import AuthService
from socialmedia.api.blueprints import authentication_blueprint
from socialmedia.responses import get_login_response, get_register_response, get_refresh_response, get_logout_response
from ...decorators import handle_app_errors
from ...utils import check_request_content_type

__all__ = []


@authentication_blueprint.route('/login', methods=['POST'])
@handle_app_errors
def login():
    request_body = check_request_content_type(request=request)

    access_token, refresh_token, user = AuthService.login(user_data=request_body)
    response, code = get_login_response(user=user)
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)
    return response, code


@authentication_blueprint.route('/register', methods=['POST'])
@handle_app_errors
def register():
    request_body = check_request_content_type(request=request)

    access_token, refresh_token, user = AuthService.register(user_data=request_body)
    response, code = get_register_response(user=user)
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)
    return response, code


@authentication_blueprint.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)
@handle_app_errors
def refresh():
    user_id = int(get_jwt_identity().get('id'))
    access_token, refresh_token = AuthService.refresh_tokens(user_id=user_id)
    response, code = get_refresh_response()
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)
    return response, code


@authentication_blueprint.route('/logout', methods=['GET'])
@jwt_required()
@handle_app_errors
def logout():
    user_id = int(get_jwt_identity().get('id'))
    AuthService.logout(user_id=user_id)
    response, code = get_logout_response()
    unset_jwt_cookies(response=response)
    return response, code
