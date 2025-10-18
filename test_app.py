import app

def test_home_page():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    # Check for the title of your DevOps site
    assert b"DevOps Unleashed" in response.data