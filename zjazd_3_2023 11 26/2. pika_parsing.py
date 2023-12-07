import json

def load_pikachu():
    pika_file = open("pika.json")
    pikachu_dict = json.load(pika_file)
    return pikachu_dict

pikachu = load_pikachu()


"""
print(f'Name: {pikachu_dictionary["name"]}')
print(f'Weight: {pikachu_dictionary["weight"]}')
print(f'Height: {pikachu_dictionary["height"]}')"""


"""print(json.dumps(pikachu_dictionary, indent=4))"""
"""pika_file = open("pika.json")
print(f'Name: {json.load(pika_file)["name"]}')

pika_file = open("pika.json")
print(f'Weight: {json.load(pika_file)["weight"]}')

pika_file = open("pika.json")
print(f'Height: {json.load(pika_file)["height"]}')"""

print(pikachu["moves"][4]["move"]["name"])

"""Utworzyć listę nazw wszytskich movesetów pikachu"""

moves_list = []
for i in pikachu["moves"]:
    moves_list.append(i["move"]["name"])

for i in moves_list:
    print(i)

"""Utwórz listę umiejętnosci pikachu, które są nieukryte """

abilities_list = []

for i in pikachu["abilities"]:
    if i["is_hidden"] is False:
        abilities_list.append(i["ability"]["name"])
print(abilities_list)


