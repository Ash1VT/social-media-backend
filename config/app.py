from pathlib import Path

from dotenv import dotenv_values

__all__ = ['DevelopmentConfig', 'ProductionConfig']

basedir = Path.cwd()


class Config:
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{dotenv_values().get('DATABASE_USER')}:" \
                              f"{dotenv_values().get('DATABASE_PASSWORD')}@" \
                              f"127.0.0.1:{dotenv_values().get('DATABASE_PORT')}/" \
                              f"{dotenv_values().get('DATABASE_NAME')} "
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass
