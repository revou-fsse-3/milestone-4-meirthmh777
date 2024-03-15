from app.utils.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, func, DECIMAL


class AccountModel (db.Model):
    __tablename__ = "accounts"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer)
    account_type = mapped_column(String(255))
    account_number = mapped_column(String(255))
    balance = mapped_column(DECIMAL(10,2))
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at =mapped_column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self):
        return f'<Account {self.id}>'
    
