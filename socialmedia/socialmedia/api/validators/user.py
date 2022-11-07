from marshmallow import Schema, fields, validates, ValidationError


class UserLoginSchema(Schema):
    username = fields.String(required=True,
                             error_messages={
                                 'required': 'Username is a mandatory field'
                             })
    password = fields.String(required=True,
                             error_messages={
                                 'required': 'Password is mandatory field'
                             })

    @validates('username')
    def validate_username(self, username):
        username_length = len(username)
        if not username_length:
            raise ValidationError('Username is a mandatory field')
        if username_length < 5:
            raise ValidationError('Username must have at least 5 characters')
        if username_length > 30:
            raise ValidationError('Username can\'t have more than 30 characters')

    @validates('password')
    def validate_password(self, password):
        password_length = len(password)
        if not password_length:
            raise ValidationError('Username is a mandatory field')
        if password_length < 5:
            raise ValidationError('Password must have at least 5 characters')
        if password_length > 30:
            raise ValidationError('Password can\'t have more than 30 characters')


class UserRegistrationSchema(Schema):
    first_name = fields.String(required=True,
                               error_messages={
                                   'required': 'First name is a mandatory field',
                               })
    last_name = fields.String(required=True,
                              error_messages={
                                  'required': 'Last name is a mandatory field'
                              })
    username = fields.String(required=True,
                             error_messages={
                                 'required': 'Username is a mandatory field'
                             })
    email = fields.Email(required=True,
                         error_messages={
                             'required': 'Email is a mandatory field',
                             'invalid': 'String is not a email'
                         })

    password = fields.String(required=True,
                             error_messages={
                                 'required': 'Password is mandatory field'
                             })

    @validates('first_name')
    def validate_first_name(self, first_name):
        first_name_length = len(first_name)
        if first_name_length < 5:
            raise ValidationError('First name must have at least 5 characters')
        if first_name_length > 30:
            raise ValidationError('First name can\'t have more than 30 characters')

    @validates('last_name')
    def validate_last_name(self, last_name):
        last_name_length = len(last_name)
        if last_name_length < 5:
            raise ValidationError('Last name must have at least 5 characters')
        if last_name_length > 30:
            raise ValidationError('Last name can\'t have more than 40 characters')

    @validates('username')
    def validate_username(self, username):
        username_length = len(username)
        if username_length < 5:
            raise ValidationError('Username must have at least 5 characters')
        if username_length > 30:
            raise ValidationError('Username can\'t have more than 30 characters')

    @validates('password')
    def validate_password(self, password):
        username_length = len(password)
        if username_length < 5:
            raise ValidationError('Password must have at least 5 characters')
        if username_length > 30:
            raise ValidationError('Password can\'t have more than 30 characters')
