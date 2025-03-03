import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1fff7c9b7a8e2218f1d9b3d7bad85945'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
BODY_create = {
    "name": "Кеша",
    "photo_id": 55
}
BODY_change = {
    "pokemon_id": "249771",
    "name": "Вуди",
    "photo_id": 55
}
BODY_catch = {
    "pokemon_id": "249771"
}


'''responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_create)
print(responce_create.text)'''

'''responce_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_change)
print(responce_change.text)'''

responce_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_catch)
print(responce_catch.text)