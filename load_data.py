from sqlalchemy.orm import Session
from database import engine
import csv
from models import Movie, Rating, Tag, Link

def load_movies(csv_path):
    with Session(engine) as session:
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            movies: list[Movie] = []
            for row in reader:
                movies.append(
                    Movie(
                        movieId=int(row["movieId"]),
                        title=row["title"],
                        genres=row["genres"],
                    )
                )
    session.add_all(movies)
    session.commit()

def load_links(csv_path: str):
    with Session(engine) as session:
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            links: list[Link] = []
            for row in reader:
                links.append(
                    Link(
                        movieId=int(row["movieId"]),
                        imdbId=row["imdbId"],
                        tmdbId=row["tmdbId"],
                    )
                )
        session.add_all(links)
        session.commit()

def load_ratings(csv_path: str):
    with Session(engine) as session:
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            ratings: list[Rating] = []
            for row in reader:
                ratings.append(
                    Rating(
                        userId=int(row["userId"]),
                        movieId=int(row["movieId"]),
                        rating=float(row["rating"]),
                        timestamp=int(row["timestamp"]),
                    )
                )
        session.add_all(ratings)
        session.commit()


def load_tags(csv_path: str):
    with Session(engine) as session:
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            tags: list[Tag] = []
            for row in reader:
                tags.append(
                    Tag(
                        userId=int(row["userId"]),
                        movieId=int(row["movieId"]),
                        tag=row["tag"],
                        timestamp=int(row["timestamp"]),
                    )
                )
        session.add_all(tags)
        session.commit()

if __name__ == "__main__":
    load_movies("/Users/marek/Downloads/database/movies.csv")
    load_links("/Users/marek/Downloads/database/links.csv")
    load_ratings("/Users/marek/Downloads/database/ratings.csv")
    load_tags("/Users/marek/Downloads/database/tags.csv")
