from app.utils.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, func, DECIMAL
# import bcrypt


class AccountModel (db.Model):
    __tablename__ = "accounts"
    # From MySqLworkbench
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer)
    account_type = mapped_column(String(255))
    account_number = mapped_column(String(255))
    balance = mapped_column(DECIMAL(10,2))
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at =mapped_column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self):
        return f'<Account {self.id}>'
    
     # hashing password
    # def set_password(self, password):
    #     self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    # # check password in system
    # def check_password(self, password):
    #     return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
