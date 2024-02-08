from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from .base import Base


class Dealer(Base):
    __tablename__ = "dealers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dealer_name = Column(String, nullable=False)
    account_number = Column(String, nullable=False)

    # Fields for managing creation, updates, and deletions
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    orders = relationship("Order", back_populates="dealer", passive_deletes="all")

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
