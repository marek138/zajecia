import pytest

def test_movies_get_list_returns_fixture_count(client):
    r = client.get("/movies")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 2  # (a)


def test_movies_get_item_ok(client):
    r = client.get("/movies/1")
    assert r.status_code == 200  # (b)
    data = r.json()
    assert data["movieId"] == 1
    assert data["title"] == "M1"
    assert data["genres"] == "A"


def test_movies_get_item_404(client):
    r = client.get("/movies/999")
    assert r.status_code == 404  # (c)
    assert "detail" in r.json()


def test_movies_post_adds_new_row(client):
    payload = {"movieId": 3, "title": "M3", "genres": "C"}
    r = client.post("/movies", json=payload)
    assert r.status_code == 201  # (d)
    created = r.json()
    assert created["movieId"] == 3
    assert created["title"] == "M3"

    r2 = client.get("/movies")
    assert r2.status_code == 200
    assert len(r2.json()) == 3


def test_movies_put_updates_row(client):
    payload = {"title": "M1-upd", "genres": "X"}
    r = client.put("/movies/1", json=payload)
    assert r.status_code == 200  # (e)
    updated = r.json()
    assert updated["movieId"] == 1
    assert updated["title"] == "M1-upd"
    assert updated["genres"] == "X"

    r2 = client.get("/movies/1")
    assert r2.status_code == 200
    assert r2.json()["genres"] == "X"


def test_movies_delete_removes_row(client):
    r = client.delete("/movies/2")
    assert r.status_code == 204

    r2 = client.get("/movies/2")
    assert r2.status_code == 404
    assert "detail" in r2.json()

    r3 = client.get("/movies")
    assert r3.status_code == 200
    assert len(r3.json()) == 1
