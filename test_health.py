from fastapi.testclient import TestClient
from server import app
client=TestClient(app)
def test_health(): assert client.get("/api/").json()=={"service":"Afuopulse","ok":True}
def test_plans(): assert {p["tier"] for p in client.get("/api/billing/plans").json()["plans"]}=={"regional","national"}
