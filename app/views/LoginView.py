from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.UserSchemas import UserBaseSchemas
from app.models.UserModel import UserModel
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token
from http import HTTPStatus
from datetime import timedelta

blp = Blueprint('/login', __name__)

@blp.route('/login', methods=['POST'])
class LoginView(MethodView):
    @blp.arguments(UserBaseSchemas)
    def post(self, item_data):
        print(item_data)
        print('get hit')
        try :
            match_user:UserModel = UserModel.query.filter(UserModel.email==item_data['email']).first()
            print('query get hit')
            if match_user == None:
                abort(HTTPStatus.CONFLICT, message="user not found")
            if match_user.check_password(item_data['password'])==False:
                abort(HTTPStatus.CONFLICT, message="wrong password")
            access_token = create_access_token(identity=match_user.id,fresh=True, expires_delta=timedelta(days=7))
            return {"access_token": access_token, }
        except SQLAlchemyError as e:
            print(e)
            abort(HTTPStatus.CONFLICT, message="failed to insert account")

