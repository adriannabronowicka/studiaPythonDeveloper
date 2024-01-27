import random
import requests
import httpx
from pathlib import Path


def get_random_pokemon():
    pokemon_id = random.randint(1, 151)
    response = httpx.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon_data = response.json()
    return pokemon_data


def download_png(url: str, filename: str):
    response = httpx.get(url)
    png_file = open(Path(__file__).parent / "pngs" / filename, "wb")
    png_file.write(response.content)


"""Ściągnij png losowego pokemona"""


def download_pnf_of_random_pokemon():
    data = get_random_pokemon()
    name = data["name"]
    png_url = data['sprites']['other']['official-artwork']['front_default']
    download_png(png_url, name + '.png')


download_pnf_of_random_pokemon()



