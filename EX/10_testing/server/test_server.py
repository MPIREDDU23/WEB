#!/opt/homebrew/bin/python3

from server import app
import pytest, httpx
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_item_valid():
    response = client.post("/items/", json={"name": "Book", "price": 5})
    assert response.status_code == 200
    assert response.json() == {"item received": {"name": "Book", "price": 5}}

def test_create_item_invalid():
    # invalid price
    response = client.post("/items/", json={"name": "Book", "price": -5})
    assert response.status_code == 422
    
    # invalid name
    response = client.post("/items/", json={"name": "B", "price": 5})
    assert response.status_code == 422

    # both invalid
    response = client.post("/items/", json={"name": "B", "price": -5})
    assert response.status_code == 422

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_root_invalid():
    # Simulate an invalid request
    response = client.get("/invalid")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}