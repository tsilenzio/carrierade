from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base


class Dealer(Base):
    __tablename__ = "dealers"

    dealer_id = Column(Integer, primary_key=True, autoincrement=True)
    dealer_name = Column(String, nullable=False)
    account_number = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    # Relationship to Orders
    orders = relationship("Order", back_populates="dealer")
