# zad 4: zamień pary elementów w liście 'a' miejscami,
# czyli powinno wyjść: [52, 2, 7, 5, 67, 12, 31, 22]
a = [2, 52, 5, 7, 12, 67, 22, 31]
print(f"The list a looks like this {a}")

b = [number for number in a]

list_lenght = len(a)
number_of_pairs = list_lenght // 2
n = 0
"""
for i in range(number_of_pairs):
    b[n] = a[n+1]
    b[n+1] = a[n]
    n += 2

print(f"The list a looks like this {a}")
print(f"The sorted list looks like this: {b}")
"""
for j in range(number_of_pairs):
    a[n], a[n+1] = a[n+1], a[n]
    n += 2
print(f"The list a looks like this {a}")


