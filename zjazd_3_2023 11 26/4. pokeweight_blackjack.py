import random
from dataclasses import dataclass

import httpx


@dataclass
class Pokemon:
    name: str
    weight: int


def get_random_pokemon() -> Pokemon:
    pokemon_id = random.randint(1, 151)
    response = httpx.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon_data = response.json()
    return Pokemon(pokemon_data["name"], pokemon_data["weight"])


"""
Jesteśmy w pokoju z pokemonami, i mamy wielką walizkę, w której
możemy unieść 2000 wagi.
Program spyta nas, czy chcemy wziąć kolejnego pokemona do walizki.
Jeśli powiemy "tak", to poinformuje nas ile miejsca w walizce nam zostało.
Jeśli powiemy "tak" i skończy nam się miejsce w walizce - PRZEGRYWAMY.
Jeśli powiemy "nie", gra się kończy i printuje pokemony, które
zabieramy ze sobą do domu ^_^

"""
capacity = 2000
suitcase = []
pokemon = get_random_pokemon()
print(f"You took {pokemon.name}")
suitcase.append(pokemon.name)
capacity -= pokemon.weight
print(f"Capacity your suitcase is {capacity}.")
while True:
    if input("Do you want to take another pokemon with you? (y/n): ") != "y":
        print(f"You took{suitcase} with you, congrats :)")
        break
    pokemon = get_random_pokemon()
    print(f"You took {pokemon.name}")
    suitcase.append(pokemon.name)
    capacity -= pokemon.weight
    if capacity <= 0:
        print("Game over! You lost!")
        break
    else:
        print(f"You still have {capacity} in your suitcase.")

