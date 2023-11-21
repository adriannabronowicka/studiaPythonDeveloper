def podatek(zarobki, liczba_dzieci):
    podatek_do_zapłaty = zarobki * 0.2 - 100 * liczba_dzieci
    return podatek_do_zapłaty

x = podatek(4000, 3)


def zdrowie_czlowieka(wiek, waga, samopoczucie):
    wspol_zdrowia = 0
    if wiek <= 18:
        wspol_zdrowia += 5
    elif wiek > 18 and wiek <= 30:
        wspol_zdrowia += 4
    elif wiek > 30 and wiek <= 40:
        wspol_zdrowia += 3
    elif wiek > 40 and wiek <= 50:
        wspol_zdrowia += 2
    else:
        wspol_zdrowia += 1

    if waga <= 100:
        wspol_zdrowia += 1
    else:
        wspol_zdrowia += 0

    wspol_zdrowia += samopoczucie

    return wspol_zdrowia

wiek = int(input("Wprowadź wiek: "))
waga = int(input("Wprowadź wagę: "))
samopoczucie = int(input("Wprowadź samopoczucie: "))


x = zdrowie_czlowieka(wiek, waga, samopoczucie)
if x > 5:
    print("Dostaniesz ubezpieczenie")
else:
    print("Nie dostaniesz ubezpieczenia")

def mnozenie(a, b):
    return round(a * b)

print(mnozenie(5.5, 5.5))