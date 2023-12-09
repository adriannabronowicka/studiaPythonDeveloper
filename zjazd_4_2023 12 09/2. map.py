a = ["4", "6", "2"]

"""mapowanie"""
result = list(map(int, a))
print(result)

"""kopiowanie"""
from copy import copy

b = copy(a)

"""kopiowanie bez importu"""
b = a.copy()