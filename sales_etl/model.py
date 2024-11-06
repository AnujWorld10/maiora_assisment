from sqlalchemy import Column, Integer, Float, String
from database import Base

class SalesData(Base):
    __tablename__ = 'sales_data'

    OrderId = Column(Integer, primary_key=True, index=True)
    OrderItemId = Column(Integer)
    QuantityOrdered = Column(Integer)
    ItemPrice = Column(Float)
    PromotionDiscount = Column(Float)
    total_sales = Column(Float)
    region = Column(String(1))
    net_sale = Column(Float)
