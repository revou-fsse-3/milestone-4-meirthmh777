# from flask import Blueprint, request, redirect
# from app.models.UserModel import UserModel
# from app.connectors.connector import engine
# from sqlalchemy.orm import sessionmaker, Session
# from flask_login import login_user, logout_user


# user_register = Blueprint('user_register_routes', __name__)


# # get the user
# @user_register.route('/register', methods=['POST'])
# def user_do_register():
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']

#     new_user_register = UserModel(username=username, email=email)
#     new_user_register.set_password(password)

#     connection = engine.connect()
#     Session = sessionmaker(connection)
#     session = Session()
#     session.begin()
#     try:
#         # operation success
#         session.add(new_user_register)
#         session.commit()
#         return redirect('/login')
#     except Exception as e :
#         session.rollback()
#         print(e)
#         return{'message': 'new user failed do register'}

# # check email if already exists
# @user_register.route('/login', methods=['POST'])
# def user_do_login():
#     # search user
#     connection = engine.connect()
#     Session = sessionmaker(connection)
#     session = Session()

#     try:
#         user_try_login = session.query(UserModel).filter(UserModel.email==request.form['email']).first()
#         # check email is exists in db
#         if user_try_login == None:
#             return{"message" : "email not found"}
#         # check password
#         if not user_try_login.check_password(request.form['password']):
#             return{"message" : "wrong password"}
#         # if login ok
#         login_user(user_try_login, remember=False)
#         return redirect('/accounts')
#     except Exception as e:
#         session.rollback()
#         print(e)
#         return{'message': 'user failed do login'}
    
# # logout
# @user_register.route('/logout', methods=['GET'])
# def user_do_logput():
#     logout_user()
#     return redirect('/login')

# # update certain user by it's id
# # @user_register.route('/users/<id>', methods=['PUT'])
# # def update_user(id):
# #     session = Session()
# #     session.begin()
# #     try:
# #         user_to_update = session.query(UserModel).filter(UserModel.id==id).first()
# #         user_to_update.name = request.form['name']
# #         user_to_update.role = request.form['role']
# #         user_to_update.schedule = request.form['schedule']
# #         session.commit()
# #     except Exception as e:
# #         session.rollback()
# #         print(e)
# #         return{'message': 'update user failed'}
# #     return{'message': 'update user success'}
