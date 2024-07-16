# tests/conftest.py

import pytest
from app import create_app, db
from app.models import User, Doctor, Appointment

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()  # Creates test database tables
            yield testing_client  # Provides the client to the tests
            db.session.remove()  # Cleans up after tests
            db.drop_all()  # Drops all tables after tests

@pytest.fixture(scope='module')
def new_user():
    user = User(username='testuser', email='testuser@example.com')
    user.set_password('Password123')
    return user
