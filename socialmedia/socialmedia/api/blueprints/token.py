from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, get_jti, jwt_required, \
    set_access_cookies, set_refresh_cookies

from socialmedia.socialmedia.api.repositories import UserRepository
from socialmedia.socialmedia.api.services import create_token_pair

token_blueprint = Blueprint(name="token_blueprint", import_name=__name__)


@token_blueprint.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh_token():
    print('refresh')
    token_sub: dict = get_jwt_identity()
    user_id = token_sub.get('id')

    access_token, refresh_token = create_token_pair(data=token_sub)

    user = UserRepository.get_by_id(id=user_id)

    refresh_token_jti = get_jti(encoded_token=refresh_token)

    UserRepository.update(user, refresh_token_jti=refresh_token_jti)

    response = jsonify(
        {'success': True,
         'user': {
             'id': user.id,
             'username': user.username
         }})

    response.set_cookie('access_token_cookie',
                        value=access_token,
                        httponly=False)
    response.set_cookie('refresh_token_cookie',
                        value=refresh_token,
                        httponly=True)
    return response, 200


@token_blueprint.route('/check', methods=['GET'])
@jwt_required()
def check():
    return jsonify({'success': True}), 200
