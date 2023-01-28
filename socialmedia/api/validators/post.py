from marshmallow import Schema, fields, validate

from socialmedia.constants import MIN_TITLE_LENGTH, MAX_TITLE_LENGTH, MIN_TITLE_ERROR_STRING, MAX_TITLE_ERROR_STRING, \
    TITLE_EMPTY_ERROR_STRING, BODY_EMPTY_ERROR_STRING

__all__ = ['PostSchema']


class PostSchema(Schema):
    title = fields.String(required=True, validate=validate.And(
        validate.Length(min=MIN_TITLE_LENGTH, error=MIN_TITLE_ERROR_STRING),
        validate.Length(max=MAX_TITLE_LENGTH, error=MAX_TITLE_ERROR_STRING)
    ), error_messages={
        'required': TITLE_EMPTY_ERROR_STRING
    })

    body = fields.String(required=True, error_messages={
        'required': BODY_EMPTY_ERROR_STRING
    })

    user_id = fields.Integer()
