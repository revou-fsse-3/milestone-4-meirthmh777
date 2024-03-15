from marshmallow import Schema, fields

class TransactionResponseSchemas(Schema):
    id = fields.Int(dump_only=True)
    from_account_id = fields.Int()
    to_account_id = fields.Int()
    amount = fields.Decimal(places=2)
    type_transaction = fields.Str()
    description_transaction = fields.Str()
    created_at = fields.DateTime()

class TransactionCreateSchemas(Schema):
    from_account_id = fields.Int()
    to_account_id = fields.Int()
    amount = fields.Decimal(places=2)
    type_transaction = fields.Str()
    description_transaction = fields.Str()

