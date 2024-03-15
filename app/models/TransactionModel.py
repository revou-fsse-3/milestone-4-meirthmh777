from app.utils.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, func, DECIMAL


class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    from_account_id = mapped_column(Integer)
    to_account_id = mapped_column(Integer)
    amount = mapped_column(DECIMAL(10,2))
    type_transaction = mapped_column(String(255))
    description_transaction = mapped_column(String(255))
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self):
        return f'<Transaction {self.id}>'