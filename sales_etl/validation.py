from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from models import SalesData  # Import your model

DATABASE_URL = 'mysql+mysqlconnector://root:mysql@localhost/maiora_assessment'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def count_records():
    with SessionLocal() as db:
        count = db.query(func.count(SalesData.order_id)).scalar()
        print(f"Total records: {count}")

def total_sales_by_region(region):
    with SessionLocal() as db:
        total_sales = db.query(func.sum(SalesData.total_sales)).filter(SalesData.region == region).scalar()
        print(f"Total sales in {region}: {total_sales}")

def average_sales_amount():
    with SessionLocal() as db:
        average = db.query(func.avg(SalesData.net_sale)).scalar()
        print(f"Average sales amount: {average}")

def check_duplicates():
    with SessionLocal() as db:
        duplicates = db.query(SalesData.order_id).group_by(SalesData.order_id).having(func.count(SalesData.order_id) > 1).all()
        print(f"Duplicate OrderIds: {duplicates}")

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from models import SalesData  # Import your model

DATABASE_URL = 'mysql+mysqlconnector://root:mysql@localhost/maiora_assessment'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def count_records():
    with SessionLocal() as db:
        count = db.query(func.count(SalesData.order_id)).scalar()
        print(f"Total records: {count}")

def total_sales_by_region(region):
    with SessionLocal() as db:
        total_sales = db.query(func.sum(SalesData.total_sales)).filter(SalesData.region == region).scalar()
        print(f"Total sales in {region}: {total_sales}")

def average_sales_amount():
    with SessionLocal() as db:
        average = db.query(func.avg(SalesData.net_sale)).scalar()
        print(f"Average sales amount: {average}")

def check_duplicates():
    with SessionLocal() as db:
        duplicates = db.query(SalesData.order_id).group_by(SalesData.order_id).having(func.count(SalesData.order_id) > 1).all()
        print(f"Duplicate OrderIds: {duplicates}")
