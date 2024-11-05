from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Joke(Base):
    __tablename__ = 'jokes'
    id = Column(Integer, primary_key=True)
    category = Column(String)
    joke_type = Column(String)
    joke_text = Column(String)
    nsfw = Column(Boolean)
    political = Column(Boolean)
    sexist = Column(Boolean)
    safe = Column(Boolean)
    lang = Column(String)

def create_database(db_url='mysql+mysqlconnector://root:mysql@localhost/maiora_assessment'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
