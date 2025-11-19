from fastapi import FastAPI
import  csv

app = FastAPI()

class Movie:
    def __init__(self,movieId: int, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres

def load_movies(filename: str) -> list[Movie]:
    movies: list[Movie] = []
    with open(filename) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            movie = Movie(
                movieId=int(row["movieId"]),
                title=row["title"],
                genres=row["genres"]
            )
            movies.append(movie)
    return movies

class Rating:
    def __init__(self, userId: int, movieId: int, rating: float, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

def load_ratings(filename: str) -> list[Rating]:
    ratings: list[Rating] = []
    with open(filename) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            rating = Rating(
                userId=int(row['userId']),
                movieId=int(row["movieId"]),
                rating=float(row['rating']),
                timestamp=int(row['timestamp'])
            )
            ratings.append(rating)
    return ratings

class Link:
    def __init__(self, movieId: int, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

def load_links(filename: str) -> list[Link]:
    links: list[Link] = []
    with open(filename) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            link = Link(
                movieId=int(row["movieId"]),
                imdbId=row['imdbId'],
                tmdbId=row['tmdbId']
            )
            links.append(link)
    return links

class Tag:
    def __init__(self, userId: int, movieId: int, tag: str, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

def load_tags(filename: str) -> list[Tag]:
    tags: list[Tag] = []
    with open(filename) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            tag = Tag(
                userId=int(row['userId']),
                movieId=int(row["movieId"]),
                tag=row['tag'],
                timestamp=int(row['timestamp'])
            )
            tags.append(tag)
    return tags

@app.get("/")
def read_root():
    return {"hello": "world"}
@app.get("/movies")
def get_movies():
    movies = load_movies("/Users/marek/Downloads/database/movies.csv")
    serialized_movies = [movie.__dict__ for movie in movies]
    return serialized_movies

@app.get('/ratings')
def get_ratings():
    ratings = load_ratings('/Users/marek/Downloads/database/ratings.csv')
    serialized_ratings = [rating.__dict__ for rating in ratings]
    return serialized_ratings

@app.get('/links')
def get_links():
    links = load_links('/Users/marek/Downloads/database/links.csv')
    serialized_links = [link.__dict__ for link in links]
    return serialized_links

@app.get('/tags')
def get_tags():
    tags = load_tags('/Users/marek/Downloads/database/tags.csv')
    serialized_tags = [tag.__dict__ for tag in tags]
    return serialized_tags



