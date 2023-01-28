from datetime import datetime
from setup.database import db

user_liked_posts = db.Table('UserLikedPosts',
                            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                            db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                            )

user_disliked_posts = db.Table('UserDislikedPosts',
                               db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                               db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                               )

user_liked_comments = db.Table('UserLikedComments',
                               db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                               db.Column('comment_id', db.Integer, db.ForeignKey('comment.id')),
                               )

user_disliked_comments = db.Table('UserDislikedComments',
                                  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                                  db.Column('comment_id', db.Integer, db.ForeignKey('comment.id')),
                                  )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)

    registered_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_tokens = db.relationship('UserTokens', backref='user', uselist=False, lazy='select',
                                  cascade='all, delete, delete-orphan')

    posts = db.relationship('Post', backref='user', lazy='dynamic', cascade='all, delete, delete-orphan')

    liked_posts = db.relationship('Post', secondary=user_liked_posts, back_populates='liked_users', viewonly=True,
                                  lazy='dynamic')
    disliked_posts = db.relationship('Post', secondary=user_disliked_posts, back_populates='disliked_users',
                                     viewonly=True,
                                     lazy='dynamic')

    liked_comments = db.relationship('Comment', secondary=user_liked_comments, back_populates='liked_users',
                                     viewonly=True, lazy='dynamic')
    disliked_comments = db.relationship('Comment', secondary=user_disliked_comments, back_populates='disliked_users',
                                        viewonly=True, lazy='dynamic')

    comments = db.relationship('Comment', backref='user', lazy='dynamic', cascade='all, delete, delete-orphan')


class UserTokens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access_token_jti = db.Column(db.String, nullable=True)
    refresh_token_jti = db.Column(db.String, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    liked_users = db.relationship('User', secondary=user_liked_posts, back_populates='liked_posts', lazy='dynamic')
    disliked_users = db.relationship('User', secondary=user_disliked_posts, back_populates='disliked_posts',
                                     lazy='dynamic')

    comments = db.relationship('Comment', backref='post', lazy='dynamic', cascade='all, delete, delete-orphan')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)

    comment_answers = db.relationship('Comment', remote_side='Comment.comment_id', back_populates='comment',
                                      uselist=True, lazy='dynamic', cascade='all, delete, delete-orphan')

    comment = db.relationship('Comment', remote_side='Comment.id', back_populates='comment_answers',
                              uselist=False)

    liked_users = db.relationship('User', secondary=user_liked_comments, back_populates='liked_comments', lazy='dynamic')
    disliked_users = db.relationship('User', secondary=user_disliked_comments, back_populates='disliked_comments',
                                     lazy='dynamic')
