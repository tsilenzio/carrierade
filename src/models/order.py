from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CheckConstraint

from .base import Base


class Order(Base):
    __tablename__ = "orders"
    __table_args__ = (CheckConstraint("warranty_status IN ('Yes', 'No', 'N/A')"),)

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    dealer_id = Column(
        Integer, ForeignKey("dealers.dealer_id", ondelete="SET NULL"), nullable=True
    )
    order_number = Column(String)
    po_number = Column(String)
    ordered_at = Column(DateTime, nullable=False)
    caller = Column(String)
    phone = Column(String)
    model_number = Column(String)
    serial_number = Column(String)
    warranty_status = Column(String, nullable=False, default="N/A")
    short_description = Column(String)

    # Fields for managing creation, updates, and deletions
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    dealer = relationship("Dealer", back_populates="orders")

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
