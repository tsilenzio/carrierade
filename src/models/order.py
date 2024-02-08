from datetime import datetime

from sqlalchemy import Column, Boolean, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dealer_id = Column(
        Integer, ForeignKey("dealers.id", ondelete="SET NULL"), nullable=True
    )
    order_number = Column(String, nullable=False)
    po_number = Column(String, nullable=False)
    ordered_at = Column(DateTime, nullable=False)
    caller = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    model_number = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    warranty_status = Column(Boolean, nullable=True)
    short_description = Column(String)

    # Fields for managing creation, updates, and deletions
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    dealer = relationship("Dealer", back_populates="orders")

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
