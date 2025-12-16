def test_links_get_list_returns_fixture_count(client):
    r = client.get("/links")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 1


def test_links_get_item_ok(client):
    r = client.get("/links/1")
    assert r.status_code == 200
    data = r.json()
    assert data["movieId"] == 1
    assert data["imdbId"] == "0114709"
    assert data["tmdbId"] == "862"


def test_links_get_item_404(client):
    r = client.get("/links/999")
    assert r.status_code == 404
    assert "detail" in r.json()


def test_links_post_adds_new_row(client):
    payload = {"movieId": 2, "imdbId": "0000002", "tmdbId": "999"}
    r = client.post("/links", json=payload)
    assert r.status_code == 201
    created = r.json()
    assert created["movieId"] == 2
    assert created["tmdbId"] == "999"

    r2 = client.get("/links")
    assert r2.status_code == 200
    assert len(r2.json()) == 2


def test_links_put_updates_row(client):
    payload = {"imdbId": "777", "tmdbId": "888"}
    r = client.put("/links/1", json=payload)
    assert r.status_code == 200
    updated = r.json()
    assert updated["movieId"] == 1
    assert updated["imdbId"] == "777"
    assert updated["tmdbId"] == "888"

    r2 = client.get("/links/1")
    assert r2.status_code == 200
    assert r2.json()["tmdbId"] == "888"


def test_links_delete_removes_row(client):
    r = client.delete("/links/1")
    assert r.status_code == 204

    r2 = client.get("/links/1")
    assert r2.status_code == 404

    r3 = client.get("/links")
    assert r3.status_code == 200
    assert len(r3.json()) == 0
