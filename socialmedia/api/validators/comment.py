from marshmallow import Schema, fields, validate

from socialmedia.constants import MIN_TEXT_LENGTH, MAX_TEXT_LENGTH, MIN_TEXT_ERROR_STRING, MAX_TEXT_ERROR_STRING, \
    TEXT_EMPTY_ERROR_STRING

__all__ = ['CommentSchema']


class CommentSchema(Schema):
    text = fields.String(required=True, validate=validate.And(
        validate.Length(min=MIN_TEXT_LENGTH, error=MIN_TEXT_ERROR_STRING),
        validate.Length(max=MAX_TEXT_LENGTH, error=MAX_TEXT_ERROR_STRING)
    ), error_messages={
        'required': TEXT_EMPTY_ERROR_STRING
    })

    user_id = fields.Integer()
    post_id = fields.Integer()
    comment_id = fields.Integer(required=False)
