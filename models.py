from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = "movies"
    movieId: Mapped[int]= mapped_column(primary_key=True)
    title: Mapped[str]= mapped_column(String)
    genres: Mapped[str]= mapped_column(String)
    def __repr__(self) -> str:
        return f"Movie(movieId={self.movieId!r}, title={self.title!r}, genre={self.genres!r})"

class Rating(Base):
    __tablename__ = "ratings"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId: Mapped[int]= mapped_column(Integer)
    movieId: Mapped[int]= mapped_column(Integer)
    rating: Mapped[float]= mapped_column(Float)
    timestamp: Mapped[int]= mapped_column(Integer)

    def __repr__(self) -> str:
        return f"(id={self.id!r},userId={self.userId!r}, movieId={self.movieId!r}, rating={self.rating!r}, timestamp={self.timestamp!r})"

class Link(Base):
    __tablename__ = "links"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    movieId: Mapped[int]= mapped_column(Integer)
    imdbId: Mapped[str]= mapped_column(String)
    tmdbId: Mapped[str]= mapped_column(String)

    def __repr__(self) -> str:
        return f"Movie(id={self.id!r}, movieId={self.movieId!r}, imdbId={self.imdbId!r}, tmdbId={self.tmdbId})"

class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId: Mapped[int]= mapped_column(Integer)
    movieId: Mapped[int]= mapped_column(Integer)
    tag: Mapped[str]= mapped_column(String)
    timestamp: Mapped[int]= mapped_column(Integer)
    def __repr__(self) -> str:
        return f"Movie(id={self.id!r}, userId={self.userId!r}, movieId={self.movieId!r}, tag={self.tag}, timestamp={self.timestamp!r})"