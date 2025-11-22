import json
import pytest

from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    # Use testing client
    with app.test_client() as client:
        yield client


def test_api_mood_success(client):
    # Happy path: send a recognized mood (bored -> ludo)
    resp = client.post('/api/mood', data=json.dumps({'mood': 'bored'}), content_type='application/json')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['status'] == 'success'
    assert data.get('game') == 'ludo'
    assert 'emotion' in data


def test_api_mood_missing(client):
    # Missing mood should return a 400 error and helpful message
    resp = client.post('/api/mood', data=json.dumps({'mood': ''}), content_type='application/json')
    assert resp.status_code == 400
    data = resp.get_json()
    assert data is not None
    assert data.get('status') == 'error'