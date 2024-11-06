from sqlalchemy import Column, Integer, Float, String
from database import Base  # Assuming you have a database module with Base defined

class SalesData(Base):
    __tablename__ = 'sales_data'

    order_id = Column(Integer, primary_key=True, index=True)
    total_sales = Column(Float)
    region = Column(String)
    net_sale = Column(Float)

from sqlalchemy import Column, Integer, Float, String
from database import Base  # Assuming you have a database module with Base defined

class SalesData(Base):
    __tablename__ = 'sales_data'

    order_id = Column(Integer, primary_key=True, index=True)
    total_sales = Column(Float)
    region = Column(String)
    net_sale = Column(Float)
