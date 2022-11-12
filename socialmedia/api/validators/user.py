from marshmallow import Schema, fields, validates, validate, ValidationError
from ...constants import MIN_FIRST_NAME_LENGTH, MAX_FIRST_NAME_LENGTH, FIRST_NAME_EMPTY_ERROR_STRING, \
    MIN_FIRST_NAME_ERROR_STRING, MAX_FIRST_NAME_ERROR_STRING, \
 \
    MIN_LAST_NAME_LENGTH, MAX_LAST_NAME_LENGTH, LAST_NAME_EMPTY_ERROR_STRING, MIN_LAST_NAME_ERROR_STRING, \
    MAX_LAST_NAME_ERROR_STRING, \
 \
    MIN_USERNAME_LENGTH, MAX_USERNAME_LENGTH, USERNAME_EMPTY_ERROR_STRING, MIN_USERNAME_ERROR_STRING, \
    MAX_USERNAME_ERROR_STRING, \
 \
    EMAIL_EMPTY_ERROR_STRING, EMAIL_INVALID_ERROR_STRING, \
 \
    MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH, PASSWORD_EMPTY_ERROR_STRING, MIN_PASSWORD_ERROR_STRING, \
    MAX_PASSWORD_ERROR_STRING

__all__ = ['UserSchema']


class UserSchema(Schema):
    first_name = fields.String(required=True, validate=validate.And(
        validate.Length(min=MIN_FIRST_NAME_LENGTH, error=MIN_FIRST_NAME_ERROR_STRING),
        validate.Length(max=MAX_FIRST_NAME_LENGTH, error=MAX_FIRST_NAME_ERROR_STRING)
    ), error_messages={
        'required': LAST_NAME_EMPTY_ERROR_STRING
    })

    last_name = fields.String(required=True, validate=validate.And(
        validate.Length(min=MIN_LAST_NAME_LENGTH, error=MIN_LAST_NAME_ERROR_STRING),
        validate.Length(max=MAX_LAST_NAME_LENGTH, error=MAX_LAST_NAME_ERROR_STRING)
    ), error_messages={
        'required': LAST_NAME_EMPTY_ERROR_STRING
    })

    username = fields.String(required=True, validate=validate.And(
        validate.Length(min=MIN_USERNAME_LENGTH, error=MIN_USERNAME_ERROR_STRING),
        validate.Length(max=MAX_USERNAME_LENGTH, error=MAX_USERNAME_ERROR_STRING)
    ), error_messages={
        'required': USERNAME_EMPTY_ERROR_STRING
    })

    email = fields.String(required=True, validate=validate.And(
        validate.Email(error=EMAIL_INVALID_ERROR_STRING)
    ), error_messages={
        'required': EMAIL_EMPTY_ERROR_STRING,
    })

    password = fields.String(required=True, validate=validate.And(
        validate.Length(min=MIN_PASSWORD_LENGTH, error=MIN_PASSWORD_ERROR_STRING),
        validate.Length(max=MAX_PASSWORD_LENGTH, error=MAX_PASSWORD_ERROR_STRING)
    ), error_messages={
        'required': PASSWORD_EMPTY_ERROR_STRING
    })
