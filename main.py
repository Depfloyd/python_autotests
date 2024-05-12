import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '655510d7d1e5839d9a22c1db40113055'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "depfloyd1@yandex.ru",
    "password": "Qwe123456"
}

body_confirmation = {
    "trainer_token": "655510d7d1e5839d9a22c1db40113055"
}

body_create = {
    "name": "Жопсер",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change_name = {
    "pokemon_id": "26987",
    "name": "Zhopser",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokemon_add = {
    "pokemon_id": "26987"
}

'''
response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)
'''
'''
response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)
'''
'''
response_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)
'''

#response_list = requests.get(url=f'{URL}/pokemons', headers = HEADER, params = {'trainer_id' : 4055})
#print(response_list.text)

#response_change_name = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_change_name)
#message_for_change_name = response_change_name.json()['message']
#print(message_for_change_name)

response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_add)
print(response_add_pokeball.text)

