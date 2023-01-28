from flask_cors import CORS

from setup import app, db

from socialmedia.api.blueprints import api_blueprint

CORS(app)
app.config.from_object('config.app.DevelopmentConfig')
app.config.from_object('config.jwt.JWTConfig')
db.init_app(app)

app.register_blueprint(api_blueprint, url_prefix='/api/')
