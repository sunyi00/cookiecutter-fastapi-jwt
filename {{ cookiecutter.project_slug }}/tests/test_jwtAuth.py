from fastapi import testclient

from app.main import app

client = TestClient(app)
