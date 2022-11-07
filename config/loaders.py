from flask import jsonify

from socialmedia.socialmedia.api import UserRepository


def is_token_valid(header: dict, payload: dict):
    token_type = payload.get('type')
    token_sub: dict = payload.get('sub')

    user_id = token_sub.get('id')
    user = UserRepository.get_by_id(id=user_id)

    if not user:
        return False

    if token_type == 'access':
        return True

    token_jti = payload.get('jti')

    if user.refresh_token_jti == token_jti and token_type == 'refresh':
        return True

    return False


def token_expired_response(header: dict, payload: dict):
    return jsonify({'msg': 'expired'}), 401


def missing(str):
    return jsonify(
        {
            'status': 'fail',
            'message': str}
    ), 401
