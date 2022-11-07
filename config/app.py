from pathlib import Path

from dotenv import dotenv_values

__all__ = ['DevelopmentConfig', 'ProductionConfig']

basedir = Path.cwd()


class Config:
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(basedir / 'socialmedia' / dotenv_values().get('DATABASE_NAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass
