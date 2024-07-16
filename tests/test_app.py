# tests/test_app.py for the main application and configuragtion
def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to DocMeet" in response.data
