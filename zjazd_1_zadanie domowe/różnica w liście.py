#  znajdź parę liczb w zadanej liście, której różnica wynosi 70
a = [253, 12, -2, 53, 9, 234, 123, -94, 29, 7]

n = 70
for number_1 in a:
    for number_2 in a:
        if number_1 - number_2 == n:
            print(f"These numbers are {number_1} and {number_2}.")