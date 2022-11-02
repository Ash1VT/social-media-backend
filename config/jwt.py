from datetime import timedelta

from dotenv import dotenv_values

from socialmedia.socialmedia.db.model import User

__all__ = ['JWT_ACCESS_TOKEN_EXPIRES', 'JWT_REFRESH_TOKEN_EXPIRES',
           'JWT_SECRET_KEY', 'JWT_TOKEN_LOCATION', 'JWT_CSRF_CHECK_FORM',
           'JWT_CSRF_IN_COOKIES', 'JWT_COOKIE_CSRF_PROTECT', 'is_token_valid']

JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=5)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=10)
JWT_SECRET_KEY = dotenv_values().get('SECRET_KEY')
JWT_TOKEN_LOCATION = ['cookies']
JWT_CSRF_CHECK_FORM = False
JWT_CSRF_IN_COOKIES = False
JWT_COOKIE_CSRF_PROTECT = False


def is_token_valid(header: dict, payload: dict):
    token_type = payload.get('type')
    token_sub: dict = payload.get('sub')

    user_id = token_sub.get('id')
    user = User.query.filter_by(id=f'{user_id}').first()
    if not user:
        return False

    if token_type == 'access':
        return True

    token_jti = payload.get('jti')

    if user.refresh_token_jti == token_jti and token_type == 'refresh':
        return True

    return False
