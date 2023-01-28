from flask_jwt_extended import create_access_token, create_refresh_token, get_jti


def create_token_pair(data: dict) -> (str, str):
    return create_access_token(identity=data), create_refresh_token(identity=data)


def get_token_jti(encoded_token: str):
    return get_jti(encoded_token=encoded_token)
