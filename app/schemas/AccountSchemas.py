from marshmallow import Schema, fields

class AccountResponsSchemas(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    account_type = fields.Str()
    account_number = fields.Str()
    balance = fields.Decimal(places=2)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class AccountCreateSchemas(Schema):
    user_id = fields.Int()
    account_type = fields.Str()
    account_number = fields.Str()
    balance = fields.Decimal(places=2)

class AccountUpdateSchemas(Schema):
    account_type = fields.Str()
    account_number = fields.Str()
    balance = fields.Decimal(places=2)