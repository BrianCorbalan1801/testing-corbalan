import pytest

from flaskr.db import get_db

def test_update_user_email(client, auth, app):
    auth.login()

    assert client.get("/usermod/update-email").status_code == 200
    client.post("/usermod/update-email", data={"user_email": "x@x"})

    with app.app_context():
        db = get_db()
        user = db.execute("SELECT * FROM user WHERE id = 1").fetchone()
        assert user["user_email"] == "x@x"


def test_delete(client, auth, app):
    auth.login()
    response = client.post("/1/delete")
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute("SELECT * FROM post WHERE id = 1").fetchone()
        assert post is None