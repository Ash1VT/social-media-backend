from setup.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)

    user_tokens = db.relationship('UserTokens', backref='user', uselist=False, lazy=True)


class UserTokens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access_token_jti = db.Column(db.String, nullable=True)
    refresh_token_jti = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
