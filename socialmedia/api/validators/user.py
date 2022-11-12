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

    # @validates('first_name')
    # def validate_first_name(self, first_name: str):
    #     first_name_length = len(first_name)
    #     if first_name_length < MIN_FIRST_NAME_LENGTH:
    #         raise ValidationError(MIN_FIRST_NAME_ERROR_STRING)
    #     if first_name_length > MAX_FIRST_NAME_LENGTH:
    #         raise ValidationError(MAX_FIRST_NAME_ERROR_STRING)

    # @validates('last_name')
    # def validate_last_name(self, last_name: str):
    #     last_name_length = len(last_name)
    #     if last_name_length < MIN_LAST_NAME_LENGTH:
    #         raise ValidationError(MIN_LAST_NAME_ERROR_STRING)
    #     if last_name_length > MAX_LAST_NAME_LENGTH:
    #         raise ValidationError(MAX_LAST_NAME_ERROR_STRING)

    # @validates('username')
    # def validate_username(self, username: str):
    #     username_length = len(username)
    #     if username_length < MIN_USERNAME_LENGTH:
    #         raise ValidationError(MIN_USERNAME_ERROR_STRING)
    #     if username_length > MAX_USERNAME_LENGTH:
    #         raise ValidationError(MAX_USERNAME_ERROR_STRING)
    #
    # @validates('email')
    # def validate_email(self, email: str):
    #     email_length = len(email)
    #     if email_length < MIN_EMAIL_LENGTH:
    #         raise ValidationError(MIN_EMAIL_ERROR_STRING)
    #     if email_length > MAX_EMAIL_LENGTH:
    #         raise ValidationError(MAX_EMAIL_ERROR_STRING)

    # @validates('password')
    # def validate_password(self, password: str):
    #     password_length = len(password)
    #     if password_length < MIN_PASSWORD_LENGTH:
    #         raise ValidationError(MIN_PASSWORD_ERROR_STRING)
    #     if password_length > MAX_PASSWORD_LENGTH:
    #         raise ValidationError(MAX_PASSWORD_ERROR_STRING)
