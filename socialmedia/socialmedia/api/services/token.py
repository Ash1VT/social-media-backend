from flask_jwt_extended import create_access_token, create_refresh_token


def create_token_pair(data: dict):
    return create_access_token(identity=data), create_refresh_token(identity=data)


