from marshmallow import Schema, fields

class UserResponsSchemas(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class UserBaseSchemas(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()

class UserUpdateSchemas(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()