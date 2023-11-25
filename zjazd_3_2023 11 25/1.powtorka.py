# Ile powtarzajacych sie elementow w liscie

a = [2, 4, 2, 2, 15, 16, 5, 15]

"""def recurring_numbers(liczby):
    dublikaty = []
    unikalne_liczby = set()
    for liczba in liczby:
        if liczba in unikalne_liczby:
            dublikaty.append(liczba)
        else:
            unikalne_liczby.add(liczba)
    return dublikaty

x = [2, 4, 2, 2, 15, 16, 5, 15]
wynik = recurring_numbers(x)
print("Powtarzające się liczby:", wynik)
"""

def czy_roznica(lista):
    zbior = set(lista)
    return len(lista) - len(zbior)

print(czy_roznica(a))


