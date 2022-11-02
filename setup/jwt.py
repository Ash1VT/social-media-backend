from flask_jwt_extended import JWTManager

from . import app

jwt = JWTManager(app)
