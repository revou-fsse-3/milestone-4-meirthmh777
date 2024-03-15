from app.utils.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, func
from passlib.hash import pbkdf2_sha256
from flask_login import UserMixin

class UserModel(db.Model, UserMixin):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(255), nullable=False, unique=True)
    email = mapped_column(String(255), nullable=False, unique=True)
    password = mapped_column(String(255), nullable=False)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now())


    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)
    def check_password(self, password):
        is_password_matching = False
        try :
            is_password_matching = pbkdf2_sha256.verify(password, self.password)
        except Exception as e :
            print(e)
        return(is_password_matching)
