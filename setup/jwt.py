from flask_jwt_extended import JWTManager

from socialmedia.responses import get_token_expired_response, get_token_invalid_response, \
    get_token_missing_response, get_token_revoked_response
from socialmedia.api.jwt import check_if_token_is_revoked
from . import app

jwt = JWTManager(app)

jwt.token_in_blocklist_loader(check_if_token_is_revoked)
jwt.expired_token_loader(get_token_expired_response)
jwt.revoked_token_loader(get_token_revoked_response)
jwt.invalid_token_loader(get_token_invalid_response)
jwt.unauthorized_loader(get_token_missing_response)
