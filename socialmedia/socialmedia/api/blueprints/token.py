from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, decode_token, \
    get_jwt, set_access_cookies, set_refresh_cookies

from setup.database import db
from socialmedia.socialmedia.db.model import User
from socialmedia.socialmedia.api.services import create_token_pair

blueprint_token = Blueprint(name="blueprint_token", import_name=__name__)


@blueprint_token.route('/token', methods=['POST'])
def obtain_token_pair():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({'message': 'bad data'}), 401

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'cannot find user with such username'}), 401

    user_id = user.id

    data = {
        'username': username,
        'id': user_id
    }

    access_token, refresh_token = create_token_pair(data=data)

    user.refresh_token_jti = decode_token(refresh_token).get('jti')
    db.session.commit()

    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp, 200


@blueprint_token.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():
    token_sub: dict = get_jwt_identity()
    user_id = token_sub.get('id')

    access_token, refresh_token = create_token_pair(data=token_sub)

    user = User.query.filter_by(id=user_id).first()
    user.refresh_token_jti = decode_token(refresh_token).get('jti')
    db.session.commit()

    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp, 200


@blueprint_token.route('/test', methods=['GET'])
@jwt_required()
def testing():
    return 'It works'
