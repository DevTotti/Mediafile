import pytest

from app import app as main_app

@pytest.fixture
def app():
    yield main_app


@pytest.fixture
def client(app):
    app.config["TESTING"] = True
    client = app.test_client()
    return client