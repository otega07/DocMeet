# tests/test_routes.py

import pytest
from app import app, db
from app.models import User, Doctor, Appointment

@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('config.TestConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def test_client(test_app):
    return test_app.test_client()

def test_index_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to DocMeet" in response.data

def test_login_page(test_client):
    response = test_client.get('/users/login')
    assert response.status_code == 200
    assert b"Login" in response.data

def test_register_page(test_client):
    response = test_client.get('/users/register')
    assert response.status_code == 200
    assert b"Register" in response.data
