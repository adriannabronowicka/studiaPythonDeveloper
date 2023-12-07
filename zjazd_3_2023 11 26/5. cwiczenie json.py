import json
def load_pikachu():
    pika_file = open("pika.json")
    pikachu_dict = json.load(pika_file)
    return pikachu_dict


pikachu = load_pikachu()

print(pikachu["name"])

print(pikachu["moves"][4]["move"]["name"]) # wyjęty jeden ruch pikatchu ze słownika

moves_list =[]

"""Utworzyć listę nazw wszytskich movesetów pikachu"""
for i in pikachu["moves"]:
    moves_list.append(i["move"]["name"])
print(moves_list)


"""Utwórz listę umiejętnosci pikachu, które są nieukryte """
for j in pikachu["abilities"]:
    if j["is_hidden"] is False:
        print(j["ability"]["name"])


"""Utwórz listę held_items, version details z 1 item """
for k in pikachu["held_items"][0]["version_details"]:
    print(k["version"]["name"])


"""Utwórz listę held_items, version details z wszytskich item """
for m in pikachu["held_items"]:
    for n in m["version_details"]:
        print(n["version"]["name"])


"""Utwórz listę held_items, wszytskie item name """
for p in pikachu["held_items"]:
    print(p["item"]["name"])