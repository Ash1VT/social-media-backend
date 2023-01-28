from flask import Blueprint
from .auth import authentication_blueprint
from .user import user_blueprint
from .post import post_blueprint
from .comment import comment_blueprint

api_blueprint = Blueprint('api_blueprint', import_name=__name__)
api_blueprint.register_blueprint(authentication_blueprint, url_prefix='/')
api_blueprint.register_blueprint(post_blueprint, url_prefix='/posts')
api_blueprint.register_blueprint(user_blueprint, url_prefix='/users')
api_blueprint.register_blueprint(comment_blueprint, url_prefix='/comments')
