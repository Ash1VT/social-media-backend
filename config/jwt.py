from datetime import timedelta

from dotenv import dotenv_values


class JWTConfig:
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=5)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=10)
    JWT_SECRET_KEY = dotenv_values().get('SECRET_KEY')
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_CSRF_CHECK_FORM = False
    JWT_CSRF_IN_COOKIES = False
    JWT_COOKIE_CSRF_PROTECT = False
