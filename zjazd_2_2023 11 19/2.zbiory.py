# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających na bemowie
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na zoliborzu

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
centrum = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
krzyki = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma zbiorów ->              |
# cześć wspólna zbiorów   ->   &
# różnica zbiorów  ->          -
# różnica symetryczna  ->      ^

#sprawdź, ile osób chorowało w ostatnim roku w centrum
print(f"Chorzy w ostatnim roku w centrum to: {chorzy_rok & centrum}")
print(f"Liczba to: {len(chorzy_rok & centrum)}\n")

#ile osób z centrum chorowało w ostatnim roku
print(f"Chorzy w ostatnim roku w centrum to: {centrum & chorzy_rok}")
print(f"Liczba to: {len(centrum & chorzy_rok)}\n")

# sprawdźmy poprawność danych
# każdy, kto chorował w ostatnim miesiącu, powienien jednocześnie chorować w ostatnim roku

if len(chorzy_miesiac - chorzy_rok) > 0:
    print("dane niepoprawne")

# nikt nie powinien mieszkać jednocześnie w centrum i na krzykach
# jeśli są tacy usunać

print(f"Ludzie mieszkający w centrum i na krzykach: {centrum & krzyki}")
print(f"Liczba: {len(centrum & krzyki)} ")
if len(centrum & krzyki) > 0:
    decision = input("skad usuwamy? K/C: ")
    if decision.upper() == "K":
        krzyki -= krzyki & centrum
        print("Usunieto z Krzyków")
    elif decision.upper() == "C":
        for pesel in krzyki & centrum:
            centrum.remove(pesel)
        print("Usunieto z Centrum")
    else:
        print("Nie rozpoznano wyboru, usuwam z Krzyków")
        krzyki -= centrum

print(F"Ludzie mieszkający tylko w jednym miescu: {centrum ^ krzyki}")

#każdy chory, zdrowy, z centrum i z krzyków pownien być w bazie nfz, jesli nie ma dopisz

wszyscy = chorzy_miesiac | chorzy_rok | krzyki | centrum
NFZ |= wszyscy
print(f"Zaktualizowana lista NFZ: {NFZ}")
print(f"Ilość osób na liście: {len(NFZ)}")

# pesele żeńskie mają ostatnią cyfrę parzystą, męskie - nieparzystą
# zróbmy nowe zbiory, osobne dla mężczyzn i kobiet

woman = set()
men = set()

for pesel in NFZ:
    if pesel % 2 == 0:
        woman.add(pesel)
    else:
        men.add(pesel)
print(f"Nowy zbiór kobiet: {woman}")
print(f"Nowy zbiór mężczyzn {men}")