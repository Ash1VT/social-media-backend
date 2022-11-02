from setup import app, db, jwt
from config import JWT_ACCESS_TOKEN_EXPIRES, JWT_REFRESH_TOKEN_EXPIRES, \
    JWT_SECRET_KEY, JWT_TOKEN_LOCATION, JWT_CSRF_CHECK_FORM, JWT_CSRF_IN_COOKIES,\
    JWT_COOKIE_CSRF_PROTECT, is_token_valid
from socialmedia.socialmedia.api import blueprint_token

app.config.from_object('config.app.DevelopmentConfig')
db.init_app(app)

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = JWT_REFRESH_TOKEN_EXPIRES
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_CSRF_CHECK_FORM'] = JWT_CSRF_CHECK_FORM
app.config['JWT_CSRF_IN_COOKIES'] = JWT_CSRF_IN_COOKIES
app.config['JWT_COOKIE_CSRF_PROTECT'] = JWT_COOKIE_CSRF_PROTECT

jwt.token_verification_loader(is_token_valid)


app.register_blueprint(blueprint_token, url_prefix='/api/')
