# tests/test_users.py

from flask import url_for
from app.models import User

def test_register_new_user(test_client, new_user):
    # Register a new user
    response = test_client.post(
        '/users/register',
        data=dict(
            username=new_user.username,
            email=new_user.email,
            password='Password123',
            password2='Password123'
        ),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'Congratulations, you are now a registered user!' in response.data

def test_login_user(test_client, new_user):
    # Login as the new user
    response = test_client.post(
        '/users/login',
        data=dict(username=new_user.username, password='Password123'),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'Welcome' in response.data
    assert b'Logout' in response.data
