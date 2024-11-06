import os
import requests
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from models import Joke, create_database
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://root:mysql@localhost/maiora_assessment')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    create_database(DATABASE_URL)

@app.get("/fetch_jokes")
def fetch_jokes(db: Session = Depends(get_db)):
    url = "https://v2.jokeapi.dev/joke/Any?amount=100"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        jokes_data = response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error fetching jokes from external API")

    if 'jokes' not in jokes_data:
        raise HTTPException(status_code=500, detail="Invalid joke data received")

    jokes = jokes_data.get("jokes", [])
    
    joke_objects = []
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
        joke_objects.append(new_joke)

    try:
        db.bulk_save_objects(joke_objects)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error storing jokes in the database")

    return {"message": f"Fetched and stored {len(joke_objects)} jokes successfully!"}
