import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1fff7c9b7a8e2218f1d9b3d7bad85945'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '22880'

def test_status_code():
    response = requests.get(f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200
    
def test_trainer_name():
    response_get = requests.get(f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Tokito'
