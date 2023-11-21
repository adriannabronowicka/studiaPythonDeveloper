# zad 2: wyprintuj ile razy w tekście poniżej występuje litera 'e'
# zad 3: wyprintuj która litera występuje najczęściej

b = "pip! dwudziestu uzurpatorow dusi padalcem dwa pudle"

# 1 sposób - sprawdzenie ile razy litera "e" jest w tekście

finding_letter = "e"
count = 0

for letter in b:
    if letter == finding_letter:
        count += 1
print(f"The letter occurs {count} times")

# 2 sposób - sprawdzenie ile razy litera "e" jest w tekście
count_e = b.count("e")
print(f"The letter occurs {count_e} times")

"""
#znalezienie najczęściej występującej litery z użyciem seta,
# ale wyrzucił pierwszą literke, która występuje najczęściej
max_letters = max((b.count(letter), letter) for letter in set(b))
print(f"The most occurring letter is {max_letters}")
"""
# 3 sposób

list = [letter
        for letter in b
        if letter != " " and letter != "!"]

max_letter = max(list, key = list.count )

print(f"The most occurring letter is {max_letter}")

