def test_tags_get_list_returns_fixture_count(client):
    r = client.get("/tags")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 1


def test_tags_get_item_ok(client):
    tag_id = client.get("/tags").json()[0]["id"]

    r = client.get(f"/tags/{tag_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == tag_id
    assert data["userId"] == 10
    assert data["movieId"] == 1
    assert data["tag"] == "cool"


def test_tags_get_item_404(client):
    r = client.get("/tags/999999")
    assert r.status_code == 404
    assert "detail" in r.json()


def test_tags_post_adds_new_row(client):
    payload = {"userId": 11, "movieId": 1, "tag": "nice", "timestamp": 555}
    r = client.post("/tags", json=payload)
    assert r.status_code == 201
    created = r.json()
    assert "id" in created
    assert created["tag"] == "nice"

    r2 = client.get("/tags")
    assert r2.status_code == 200
    assert len(r2.json()) == 2


def test_tags_put_updates_row(client):
    tag_id = client.get("/tags").json()[0]["id"]
    payload = {"userId": 10, "movieId": 1, "tag": "cool-upd", "timestamp": 666}

    r = client.put(f"/tags/{tag_id}", json=payload)
    assert r.status_code == 200
    updated = r.json()
    assert updated["id"] == tag_id
    assert updated["tag"] == "cool-upd"
    assert updated["timestamp"] == 666

    r2 = client.get(f"/tags/{tag_id}")
    assert r2.status_code == 200
    assert r2.json()["tag"] == "cool-upd"


def test_tags_delete_removes_row(client):
    tag_id = client.get("/tags").json()[0]["id"]

    r = client.delete(f"/tags/{tag_id}")
    assert r.status_code == 204

    r2 = client.get(f"/tags/{tag_id}")
    assert r2.status_code == 404

    r3 = client.get("/tags")
    assert r3.status_code == 200
    assert len(r3.json()) == 0
