import app

def test_home_page():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data