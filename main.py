from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from database import engine
from models import Movie, Link, Rating, Tag

app = FastAPI()


def get_session():
    with Session(engine) as session:
        yield session

@app.get("/movies")
def get_movies(session: Session = Depends(get_session)):
    stmt = select(Movie)
    movies = session.scalars(stmt).all()

    return [
        {
            "movieId": m.movieId,
            "title": m.title,
            "genres": m.genres,
        }
        for m in movies
    ]
@app.get("/links")
def get_links(session: Session = Depends(get_session)):
    stmt = select(Link)
    links = session.scalars(stmt).all()

    return [
        {
            "movieId": l.movieId,
            "imdbId": l.imdbId,
            "tmdbId": l.tmdbId,
        }
        for l in links
    ]
@app.get("/ratings")
def get_ratings(session: Session = Depends(get_session), limit: int = 100):
    stmt = select(Rating).limit(limit)
    ratings = session.scalars(stmt).all()

    return [
        {
            "id": r.id,
            "userId": r.userId,
            "movieId": r.movieId,
            "rating": r.rating,
            "timestamp": r.timestamp,
        }
        for r in ratings
    ]
@app.get("/tags")
def get_tags(session: Session = Depends(get_session), limit: int = 100):
    stmt = select(Tag).limit(limit)
    tags = session.scalars(stmt).all()

    return [
        {
            "id": t.id,
            "userId": t.userId,
            "movieId": t.movieId,
            "tag": t.tag,
            "timestamp": t.timestamp,
        }
        for t in tags
    ]
