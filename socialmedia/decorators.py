from functools import wraps
from flask import current_app
from .errors import AppError


def handle_app_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return current_app.ensure_sync(func)(*args, **kwargs)
        except AppError as error:
            return error.response

    return wrapper
