import requests
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from models import Joke, create_database
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()

DATABASE_URL = 'mysql+mysqlconnector://root:mysql@localhost/maiora_assessment'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to manage database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    create_database()

@app.get("/fetch_jokes")
def fetch_jokes(db: Session = Depends(get_db)):
    url = "https://v2.jokeapi.dev/joke/Any?amount=100"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        jokes_data = response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error fetching jokes from external API")

    jokes = jokes_data.get("jokes", [])
    for joke in jokes:
        if joke['type'] == 'single':
            joke_text = joke['joke']
            setup = None
            delivery = None
        else:
            joke_text = None
            setup = joke.get('setup')
            delivery = joke.get('delivery')

        new_joke = Joke(
            category=joke['category'],
            joke_type=joke['type'],
            joke_text=joke_text,
            setup=setup,
            delivery=delivery,
            nsfw=joke['flags']['nsfw'],
            political=joke['flags']['political'],
            sexist=joke['flags']['sexist'],
            safe=joke['safe'],
            lang=joke['lang']
        )

        db.add(new_joke)

    try:
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error storing jokes in the database")

    return {"message": "Fetched and stored jokes successfully!"}
