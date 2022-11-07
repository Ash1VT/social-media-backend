from flask import Blueprint
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from setup import app, db, jwt
from config import is_token_valid, token_expired_response, missing
from socialmedia.socialmedia.api.blueprints import login_blueprint, \
    token_blueprint, user_blueprint

CORS(app)
app.config.from_object('config.app.DevelopmentConfig')
app.config.from_object('config.jwt.JWTConfig')
db.init_app(app)


jwt.token_verification_loader(is_token_valid)
jwt.expired_token_loader(token_expired_response)
jwt.unauthorized_loader(missing)

api_blueprint = Blueprint('api_blueprint', import_name=__name__)
api_blueprint.register_blueprint(login_blueprint, url_prefix='/login')
api_blueprint.register_blueprint(user_blueprint, url_prefix='/users')
api_blueprint.register_blueprint(token_blueprint, url_prefix='/token')

app.register_blueprint(api_blueprint, url_prefix='/api/')

