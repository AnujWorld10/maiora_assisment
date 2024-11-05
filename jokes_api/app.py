import requests
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Joke, create_database

app = FastAPI()
DATABASE_URL = 'mysql+mysqlconnector://root:mysql@localhost/maiora_assessment'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.on_event("startup")
def startup():
    create_database()

@app.get("/fetch_jokes")
def fetch_jokes():
    url = "https://v2.jokeapi.dev/joke/Any?amount=100"
    response = requests.get(url)
    jokes = response.json()
    with SessionLocal() as db:
        for joke in jokes['jokes']:
            new_joke = Joke(
                category=joke['category'],
                joke_type=joke['type'],
                joke_text=joke['joke'] if joke['type'] == 'single' else None,
                nsfw=joke['flags']['nsfw'],
                political=joke['flags']['political'],
                sexist=joke['flags']['sexist'],
                safe=joke['safe'],
                lang=joke['lang']
            )
            db.add(new_joke)
        db.commit()
    return {"message": "Fetched and stored jokes successfully!"}
