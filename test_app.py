import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_todo(client):
    todo = {'title': "테스트 할일", 'completed': False}
    response = client.post('/todos', json=todo)
    assert response.status_code == 201
    assert response.json['title'] == '테스트 할일'