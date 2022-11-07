from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jti, set_access_cookies, set_refresh_cookies

from socialmedia.socialmedia.api.services import authenticate, get_token_sub, create_token_pair, UserRepository
from socialmedia.socialmedia.api.validators import UserLoginSchema

login_blueprint = Blueprint(name="login_blueprint", import_name=__name__)


@login_blueprint.route('/', methods=['POST'], strict_slashes=False)
def login():

    # Check content-type of request
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

    errors = UserLoginSchema().validate(request_body)

    if len(errors):
        print('error')
        return jsonify(
            {
                'success': False,
                'information': {
                    'fields': list(errors.keys()),
                    'errors': errors
                }
            }), 400

    # Authenticate user

    username = request_body.get('username')
    password = request_body.get('password')
    user = authenticate(username=username, password=password)

    if not user:
        return jsonify(
            {
                'success': False,
                'information': {
                    'message': 'Username or password are invalid'
                }
        })

    # Generate new token pair
    data = get_token_sub(user_id=user.id)

    access_token, refresh_token = create_token_pair(data=data)

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
