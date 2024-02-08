from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    dealer_id = Column(Integer, ForeignKey("dealers.dealer_id"), nullable=False)
    order_number = Column(String, nullable=False)
    po_number = Column(String, nullable=False)
    ordered_at = Column(DateTime, nullable=False)
    caller = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    model_number = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    warranty_status = Column(String, nullable=False, default="N/A")
    short_description = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    # Relationship to Dealer
    dealer = relationship("Dealer", back_populates="orders")
