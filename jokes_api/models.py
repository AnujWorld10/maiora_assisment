from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Joke(Base):
    __tablename__ = 'jokes'
    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    joke_type = Column(String, nullable=False)
    joke_text = Column(String)
    setup = Column(String)
    delivery = Column(String)
    nsfw = Column(Boolean, default=False)
    political = Column(Boolean, default=False)
    sexist = Column(Boolean, default=False)
    safe = Column(Boolean, default=True)
    lang = Column(String, nullable=False)

def create_database(db_url='mysql+mysqlconnector://root:mysql@localhost/maiora_assessment'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
