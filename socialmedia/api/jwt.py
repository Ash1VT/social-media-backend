from typing import Dict

from .services import UserService

__all__ = ['check_if_token_is_revoked']


def check_if_token_is_revoked(token_header: Dict, token_payload: Dict) -> bool:
    token_type = token_payload.get('type')
    token_sub: dict = token_payload.get('sub')
    user_id = token_sub.get('id')
    user = UserService.get_by_id(user_id=user_id)

    token_jti = token_payload.get('jti')

    if user.user_tokens.access_token_jti == token_jti and token_type == 'access':
        return False

    if user.user_tokens.refresh_token_jti == token_jti and token_type == 'refresh':
        return False

    return True
