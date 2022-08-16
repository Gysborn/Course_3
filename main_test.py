import pytest
from main import app


def test_app():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    print(response.json)
    # assert response.data == render_template('index.html')
    assert len(response.json) == 8
    assert response.json[2]['pk'] == 3, "ошибкаыва"


def test_app():

    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    #print(response.json)
    # assert response.data == render_template('index.html')
    #assert len(response.json) == 1
    assert response.json['pk'] == 2, "ошибка"
