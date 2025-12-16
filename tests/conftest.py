import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session

from api import app, get_session
from models import Base, Movie, Link, Rating, Tag


@pytest.fixture()
def setup_database():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def setup_test_data(setup_database):
    with Session(setup_database) as session:
        session.add_all([
            Movie(movieId=1, title="M1", genres="A"),
            Movie(movieId=2, title="M2", genres="B"),
            Link(movieId=1, imdbId="0114709", tmdbId="862"),
            Rating(userId=10, movieId=1, rating=4.0, timestamp=111),
            Tag(userId=10, movieId=1, tag="cool", timestamp=222),
        ])
        session.commit()


@pytest.fixture()
def client(setup_database, setup_test_data):
    def override_get_session():
        s = Session(setup_database)
        try:
            yield s
        finally:
            s.close()

    app.dependency_overrides[get_session] = override_get_session
    yield TestClient(app)
    app.dependency_overrides.clear()
