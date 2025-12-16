from fastapi import FastAPI, Depends, HTTPException, status
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

@app.post("/movies", status_code=status.HTTP_201_CREATED)
def create_movie(body:dict, session: Session = Depends(get_session)):
    if session.get(Movie, body["movieId"]) is not None:
        raise HTTPException(status_code=400, detail="Movie already exists")
    movie = Movie(movieId=body["movieId"], title=body["title"],genres=body["genres"])
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie

@app.get("/movies/{movie_id}", status_code=status.HTTP_200_OK)
def get_movie(movie_id:int, session: Session = Depends(get_session)):
    movie = session.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.put("/movies/{movie_id}", status_code=status.HTTP_200_OK)
def update_movie(movie_id: int, body: dict, session: Session = Depends(get_session)):
    movie = session.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    movie.title = body["title"]
    movie.genres = body["genres"]
    session.commit()
    session.refresh(movie)
    return movie

@app.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, session: Session = Depends(get_session)):
    movie = session.get(Movie, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    session.delete(movie)
    session.commit()
    return None

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

@app.post("/links", status_code=status.HTTP_201_CREATED)
def create_link(body: dict, session: Session = Depends(get_session)):
    if session.get(Link, body["movieId"]) is not None:
        raise HTTPException(status_code=400, detail="Link already exists")
    link = Link(movieId=body["movieId"], imdbId=body["imdbId"], tmdbId=body["tmdbId"])
    session.add(link)
    session.commit()
    session.refresh(link)
    return link

@app.get("/links/{movie_id}", status_code=status.HTTP_200_OK)
def get_link(movie_id: int, session: Session = Depends(get_session)):
    link = session.get(Link, movie_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return link

@app.put("/links/{movie_id}", status_code=status.HTTP_200_OK)
def update_link(movie_id: int, body: dict, session: Session = Depends(get_session)):
    link = session.get(Link, movie_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    link.imdbId = body["imdbId"]
    link.tmdbId = body["tmdbId"]
    session.commit()
    session.refresh(link)
    return link

@app.delete("/links/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_link(movie_id: int, session: Session = Depends(get_session)):
    link = session.get(Link, movie_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    session.delete(link)
    session.commit()
    return None

@app.get("/ratings")
def get_ratings(session: Session = Depends(get_session)):
    stmt = select(Rating)
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

@app.post("/ratings", status_code=status.HTTP_201_CREATED)
def create_rating(body: dict, session: Session = Depends(get_session)):
    rating = Rating(userId=body["userId"],movieId=body["movieId"],rating=body["rating"],timestamp=body["timestamp"])
    session.add(rating)
    session.commit()
    session.refresh(rating)
    return rating

@app.get("/ratings/{rating_id}", status_code=status.HTTP_200_OK)
def get_rating(rating_id: int, session: Session = Depends(get_session)):
    rating = session.get(Rating, rating_id)
    if rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating

@app.put("/ratings/{rating_id}", status_code=status.HTTP_200_OK)
def update_rating(rating_id: int, body: dict, session: Session = Depends(get_session)):
    rating = session.get(Rating, rating_id)
    if rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    rating.userId = body["userId"]
    rating.movieId = body["movieId"]
    rating.rating = body["rating"]
    rating.timestamp = body["timestamp"]
    session.commit()
    session.refresh(rating)
    return rating

@app.delete("/ratings/{rating_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rating(rating_id: int, session: Session = Depends(get_session)):
    rating = session.get(Rating, rating_id)
    if rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    session.delete(rating)
    session.commit()
    return None


@app.get("/tags")
def get_tags(session: Session = Depends(get_session)):
    stmt = select(Tag)
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

@app.post("/tags", status_code=status.HTTP_201_CREATED)
def create_tag(body: dict, session: Session = Depends(get_session)):
    tag = Tag(
        userId=body["userId"],
        movieId=body["movieId"],
        tag=body["tag"],
        timestamp=body["timestamp"],
    )
    session.add(tag)
    session.commit()
    session.refresh(tag)
    return tag

@app.get("/tags/{tag_id}", status_code=status.HTTP_200_OK)
def get_tag(tag_id: int, session: Session = Depends(get_session)):
    tag = session.get(Tag, tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@app.put("/tags/{tag_id}", status_code=status.HTTP_200_OK)
def update_tag(tag_id: int, body: dict, session: Session = Depends(get_session)):
    tag = session.get(Tag, tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    tag.userId = body["userId"]
    tag.movieId = body["movieId"]
    tag.tag = body["tag"]
    tag.timestamp = body["timestamp"]
    session.commit()
    session.refresh(tag)
    return tag

@app.delete("/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(tag_id: int, session: Session = Depends(get_session)):
    tag = session.get(Tag, tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    session.delete(tag)
    session.commit()
    return None