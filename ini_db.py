from database import engine
from models import Base, Movie, Tag, Rating, Link


def ini_db():
    Base.metadata.create_all(engine)
if __name__== "__main__":
    ini_db()