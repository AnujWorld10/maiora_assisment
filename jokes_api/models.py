from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Joke(Base):
    __tablename__ = 'jokes'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    joke_type = Column(String, nullable=False)
    joke_text = Column(String, nullable=True)
    setup = Column(String, nullable=True)
    delivery = Column(String, nullable=True)
    nsfw = Column(Boolean, default=False)
    political = Column(Boolean, default=False)
    sexist = Column(Boolean, default=False)
    safe = Column(Boolean, default=True)
    lang = Column(String, nullable=False)

def create_database(db_url):
    from sqlalchemy import create_engine
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
