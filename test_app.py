import pytest
from ACEest_Fitness_flask import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json["status"] == "ok"

def test_add_workout(client):
    r = client.post("/workouts", json={"workout": "Run", "duration": 30})
    assert r.status_code == 201
    data = r.json
    assert data["workout"] == "Run"
