from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.TransactionSchemas import TransactionResponseSchemas, TransactionCreateSchemas
from app.models.TransactionModel import TransactionModel
from app.utils.db import db
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required

blp = Blueprint("transactions", __name__)

@blp.route("/transactions")
class TransactionsView(MethodView):
    @jwt_required()
    @blp.response(200, TransactionResponseSchemas(many=True))
    def get(self):
        items = TransactionModel.query.all()
        return items
    
    @jwt_required()
    @blp.arguments(TransactionCreateSchemas)
    @blp.response(201, TransactionResponseSchemas)
    def post(self, item_data):
        print(item_data)
        try:
            item = TransactionModel(**item_data)
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
        return item

@blp.route("/transactions/<int:transaction_id>")
class TransactionView(MethodView):
    @jwt_required()
    @blp.response(200, TransactionResponseSchemas)
    def get(self, transaction_id):
        item = TransactionModel.query.get(transaction_id)
        if not item:
            abort(404, message="transaction not found")
        return item
    