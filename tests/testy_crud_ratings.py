def test_ratings_get_list_returns_fixture_count(client):
    r = client.get("/ratings")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 1


def test_ratings_get_item_ok(client):
    rating_id = client.get("/ratings").json()[0]["id"]

    r = client.get(f"/ratings/{rating_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == rating_id
    assert data["userId"] == 10
    assert data["movieId"] == 1
    assert data["rating"] == 4.0


def test_ratings_get_item_404(client):
    r = client.get("/ratings/999999")
    assert r.status_code == 404
    assert "detail" in r.json()


def test_ratings_post_adds_new_row(client):
    payload = {"userId": 11, "movieId": 1, "rating": 5.0, "timestamp": 333}
    r = client.post("/ratings", json=payload)
    assert r.status_code == 201
    created = r.json()
    assert "id" in created
    assert created["rating"] == 5.0

    r2 = client.get("/ratings")
    assert r2.status_code == 200
    assert len(r2.json()) == 2


def test_ratings_put_updates_row(client):
    rating_id = client.get("/ratings").json()[0]["id"]
    payload = {"userId": 10, "movieId": 1, "rating": 3.5, "timestamp": 444}

    r = client.put(f"/ratings/{rating_id}", json=payload)
    assert r.status_code == 200
    updated = r.json()
    assert updated["id"] == rating_id
    assert updated["rating"] == 3.5
    assert updated["timestamp"] == 444

    r2 = client.get(f"/ratings/{rating_id}")
    assert r2.status_code == 200
    assert r2.json()["rating"] == 3.5


def test_ratings_delete_removes_row(client):
    rating_id = client.get("/ratings").json()[0]["id"]

    r = client.delete(f"/ratings/{rating_id}")
    assert r.status_code == 204

    r2 = client.get(f"/ratings/{rating_id}")
    assert r2.status_code == 404

    r3 = client.get("/ratings")
    assert r3.status_code == 200
    assert len(r3.json()) == 0
