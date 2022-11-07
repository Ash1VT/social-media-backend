from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from ..repositories import UserRepository


def create_token_pair(data: dict) -> (str, str):
    return create_access_token(identity=data), create_refresh_token(identity=data)


def get_token_sub(user_id: int) -> dict:
    user = UserRepository.get_by_id(id=user_id)
    return {
        'id': user.id,
        'username': user.username
    }
