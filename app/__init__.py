from flask import Flask, jsonify
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_login import LoginManager
from app.utils.db import db
from app.views.UsersView import blp as UsersView
from app.views.AccountsView import blp as AccountsView
from app.views.TransactionsView import blp as TransactionsView
from app.views.LoginView import blp as LoginView
from app.models.UserModel import UserModel
from flask_jwt_extended import JWTManager


from app.utils.connector import my_sql_string
load_dotenv()
def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "mbanking RESTful API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
            "OPENAPI_SWAGGER_UI_URL"
        ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = my_sql_string
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    # app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SECRET_KEY'] = 'the random string' 
    app.config["JWT_SECRET_KEY"]='the random string' 
    


    # try to migrate bcs have issue in db
    migrate = Migrate(app, db)
    jwt = JWTManager(app)
    with app.app_context():
        db.create_all()
    api = Api(app)
    # bcrypt = Bcrypt(app)
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        # Look in the database and see whether the user is an admin
        print(identity)
        print("this callback get hite")
        return {"current_id": identity}
        
        
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
    # BLUEPRINT COLLECTIONS
    api.register_blueprint(UsersView)
    api.register_blueprint(AccountsView)
    api.register_blueprint(TransactionsView)
    api.register_blueprint(LoginView)



    @app.route('/')
    def hello_universe():
        return "hello universe"

    return(app)