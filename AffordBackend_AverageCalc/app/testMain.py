import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def testGetNumbersPrimes():
    response = client.get("/numbers/primes")
    assert response.status_code == 200
    data = response.json()
    assert "numbers" in data
    assert "avg" in data

def testGetNumbersFibonacci():
    response = client.get("/numbers/fibonacci")
    assert response.status_code == 200
    data = response.json()
    assert "numbers" in data
    assert "avg" in data

def testGetNumbersEven():
    response = client.get("/numbers/even")
    assert response.status_code == 200
    data = response.json()
    assert "numbers" in data
    assert "avg" in data

def testGetNumbersRandom():
    response = client.get("/numbers/random")
    assert response.status_code == 200
    data = response.json()
    assert "numbers" in data
    assert "avg" in data

def testGetNumbersInvalid():
    response = client.get("/numbers/invalid")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid numberId"}
