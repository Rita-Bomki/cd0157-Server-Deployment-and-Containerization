'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'Rita'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjcwMzQxNTUsIm5iZiI6MTY2NTgyNDU1NSwiZW1haWwiOiJyaXRhYm9ta2lAZ21haWwuY29tIn0.onsby9KuZP5hl_ukBfftUce4g8DS31XGnyUN_Y5gFvE'
EMAIL = 'ritabomki@gmail.com'
PASSWORD = 'bethebest'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'
    # assert response.json == 'Sick'

def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
    # assert False
