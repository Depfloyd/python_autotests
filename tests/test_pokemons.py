import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '655510d7d1e5839d9a22c1db40113055'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4055'

def test_status_code():
    response = requests.get(f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Жопсер'


@pytest.mark.parametrize('key, value', [('name', 'Жопсер'), ('trainer_id', TRAINER_ID), ('id', '26990')])
def test_parametrize(key, value):
    response_parametrize = requests.get(f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value