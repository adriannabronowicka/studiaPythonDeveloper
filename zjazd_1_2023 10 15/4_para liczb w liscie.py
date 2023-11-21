#  znajdź parę liczb w zadanej liście, której suma wynosi 62

list = [253, 12, -2, 53, 9, 234, 123, -94, 29, 7]

"""
for a in list:
    for b in list:
        if a  + b == 62:
            print("Numbers:",a, b)
"""
n = 62
for i in list:
    if n - i in list:
        print(f"{i} oraz {n-i} dają razem {n}")
        break
