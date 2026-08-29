from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Summer School Day 3 Homework API"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json()["project"] == "summer-school_3-day_homework"


def test_list_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert "items" in response.json()


def test_create_and_get_item():
    create_response = client.post("/items", json={"name": "keyboard"})
    assert create_response.status_code == 201
    item_id = create_response.json()["id"]

    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "keyboard"


def test_get_item_not_found():
    response = client.get("/items/999999")
    assert response.status_code == 404


def test_search_items():
    client.post("/items", json={"name": "wireless keyboard"})
    client.post("/items", json={"name": "wireless mouse"})
    client.post("/items", json={"name": "monitor"})

    response = client.get("/items/search", params={"q": "wireless"})
    assert response.status_code == 200
    results = response.json()["items"]
    assert all("wireless" in name.lower() for name in results.values())
    assert len(results) >= 2


def test_delete_item():
    create_response = client.post("/items", json={"name": "mouse"})
    item_id = create_response.json()["id"]

    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404
