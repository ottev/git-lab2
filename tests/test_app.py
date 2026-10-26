from app import app

def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, World!"

def test_missing_page():
    assert app.test_client().get("/missing").status_code == 404

def test_about():
    response = app.test_client().get("/about")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "About this laboratory project"