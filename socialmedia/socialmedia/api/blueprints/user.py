from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, get_jti, jwt_required, \
    set_access_cookies, set_refresh_cookies

from socialmedia.socialmedia.api.validators import UserRegistrationSchema
from socialmedia.socialmedia.api.repositories import UserRepository
from socialmedia.socialmedia.api.services import generate_password_hash
from socialmedia.socialmedia.db import User

user_blueprint = Blueprint(name="user_blueprint", import_name=__name__)


@user_blueprint.route('/<id>', methods=['GET'])
@jwt_required()
def get_user(id):
    token_sub: dict = get_jwt_identity()
    user_id = token_sub.get('id')

    if user_id != int(id):
        return jsonify({'error': True}), 401

    user = UserRepository.get_by_id(user_id)

    return jsonify(
        {'success': True,
         'user': {
             'id': user.id,
             'first_name': user.first_name,
             'last_name': user.last_name,
             'username': user.username,
             'email': user.email
         }
         }), 200


@user_blueprint.route('/', methods=['POST'])
def create_user():
    content_type = request.content_type.split(' ')[0].strip(';. !?:')
    if content_type == 'multipart/form-data':
        request_body = request.form
    elif content_type == 'application/json':
        request_body = request.json
    else:
        return jsonify(
            {
                'information': 'Please use \'multipart/form-data\' or \'application/json\' content-types',
                'success': False
            }), 400

    # Validate form data
    errors = UserRegistrationSchema().validate(request_body)
    if len(errors):
        return jsonify(
            {'login': False,
             'information':
                 {'fields': list(errors.keys()),
                  'errors': errors
                  }
             }), 400

    # Create new user

    first_name = request_body.get('first_name')
    last_name = request_body.get('last_name')
    username = request_body.get('username')
    email = request_body.get('email')
    password_hash = generate_password_hash(request_body.get('password'))

    # Check if the user exists
    non_unique_fields = UserRepository.exists(
        username=username,
        email=email
    )
    if len(non_unique_fields):
        return jsonify({
            'success': False,
            'information': {
                'message': 'User already exists',
                'fields': non_unique_fields
            }
        }), 400

    # Add the user to database
    user = User(first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password_hash=password_hash)

    UserRepository.append(user)

    return jsonify({'success': True}), 200


@user_blueprint.route('/<id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    pass


@user_blueprint.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    pass
