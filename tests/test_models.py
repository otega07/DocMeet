# tests/test_models.py for the SQLAlchemy models
def test_new_user(new_user):
    assert new_user.username == 'testuser'
    assert new_user.email == 'testuser@example.com'
    assert new_user.check_password('Password123')
