from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.AccountSchemas import AccountResponsSchemas , AccountCreateSchemas, AccountUpdateSchemas 
from app.models.AccountModel import AccountModel
from app.utils.db import db
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required

blp = Blueprint("accounts", __name__)


@blp.route("/accounts")
class AccountsView(MethodView):
    @jwt_required()
    @blp.response(200, AccountResponsSchemas(many=True))
    def get(self):
        items = AccountModel.query.all()
        return items

    @jwt_required()
    @blp.arguments(AccountCreateSchemas)
    @blp.response(201, AccountResponsSchemas)
    def post(self, item_data):
        user_id = item_data['user_id']
        account_type = item_data['account_number']
        account_number = item_data['account_number']
        balance = item_data['balance']
        create_account:AccountModel = AccountModel()

        try:
            create_account.user_id = user_id
            create_account.account_type = account_type
            create_account.account_number = account_number
            create_account.balance = balance
            db.session.add(create_account)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            abort(500, message="An error occurred while inserting the item.")
        return create_account


@blp.route("/accounts/<int:account_id>")
class AccountView(MethodView):
    @jwt_required()
    @blp.response(200, AccountResponsSchemas)
    def get(self, account_id):
        item = AccountModel.query.get(account_id)
        print(item)
        if not item:
            abort(404, message="account not found")
        return item

    @jwt_required()
    @blp.arguments(AccountUpdateSchemas)
    @blp.response(201, AccountResponsSchemas)
    def put(self, item_data, account_id):
        print(item_data)
        item = AccountModel.query.get_or_404(account_id)
        for key, value in item_data.items():
            setattr(item, key, value)
        db.session.commit()
        return item
    
    @jwt_required()
    def delete(self, account_id):
        item = AccountModel.query.get_or_404(account_id)
        db.session.delete(item)
        db.session.commit()
        return{"message" : "Account is deleted"}
