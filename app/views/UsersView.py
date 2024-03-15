from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.UserSchemas import UserResponsSchemas, UserBaseSchemas, UserUpdateSchemas
from app.models.UserModel import UserModel
from app.utils.db import db
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required

blp = Blueprint("users", __name__)

@blp.route("/users")
class UsersView(MethodView):
    
    @blp.arguments(UserBaseSchemas)
    @blp.response(201, UserResponsSchemas)
    def post(self, item_data):
        username = item_data['username']
        email = item_data['email']
        password = item_data['password']
        new_user_register = UserModel(username=username, email=email)
        new_user_register.set_password(password)
        try:
            db.session.add(new_user_register)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(e)
            abort(500, message="An error occurred while inserting the item.")
        return new_user_register

@blp.route("/users/<int:user_id>")
class UserView(MethodView):
    @jwt_required()
    @blp.response(200, UserResponsSchemas)
    def get(self, user_id):
        item = UserModel.query.get(user_id)
        return item
    
    @jwt_required()
    @blp.arguments(UserUpdateSchemas)
    @blp.response(201, UserResponsSchemas)
    def put(self, item_data, user_id):
        username = item_data['username']
        email = item_data['email']
        password = item_data['password']
        print(item_data)
        match_user = UserModel.query.get_or_404(user_id)
        try:
            match_user.username = username
            match_user.email = email
            match_user.set_password(password)
            db.session.commit()
        except Exception as e:
            abort(500, message="An error occurred while updating the user.")
        # for key, value in item_data.items():
        #     setattr(item, key, value)
        # db.session.commit()
        return match_user
    
# users_view = UsersView.as_view('users')
# blp.add_url_rule('/users', view_func=login_required(users_view))
# users_view_me = UserView.as_view('users_profile')
# blp.add_url_rule('/users/me', view_func=login_required(users_view_me))
