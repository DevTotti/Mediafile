import pytest

from app import main_flask_app as main_app

@pytest.fixture
def app():
    app = main_app()
    yield app


@pytest.fixture
def client(app):
    # app.config["TESTING"] = True
    with app.test_client() as client:
        yield client