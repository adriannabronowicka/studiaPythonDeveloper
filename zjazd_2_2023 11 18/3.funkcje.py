def przywitanie1():
    print('Siema')
    print('format dysku D')

def przywitanie2(imie):
    print(f'Siema {imie[::-1]}')


def przywitanie3(imie, wiek):
    if wiek < 18:
        print('Siema')
    else:
        print(f'Dzie dobry {imie}')
a = 2
zmienna = 'Ada'
if a > 3:
    przywitanie1()
else:
    przywitanie2(zmienna)

przywitanie3('Ada', 22)

