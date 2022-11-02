import os
from pathlib import Path

from dotenv import dotenv_values

__all__ = ['DevelopmentConfig', 'ProductionConfig']
# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = Path.cwd()


class Config:
    SECRET_KEY = dotenv_values().get('SECRET_KEY')
    PASSWORD_SALT = dotenv_values().get('PASSWORD_SALT')


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(basedir / 'socialmedia' / dotenv_values().get('DATABASE_NAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
