# zad 5: zasymuluj dużego lotka -
# wylosuj 6 NIEPOWTARZAJĄCYCH SIĘ liczb od 1 do 49

import random

numbers =[]
i = 0

while i < 6:
    x = random.randint(1,49)
    if x not in numbers:
        numbers.append(x)
        print(x)
        i += 1
print(f"The numbers drawn are: {numbers}")
