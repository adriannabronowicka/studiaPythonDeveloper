"""
1. Przemnóż wszytskie liczby z listy
2. Oblicz sumę cyfr wyniku
"""



a = [4, 2, 5, 7, 2, 3]
print(f"List of numbers: {a}")


"""Rozwiązanie podstawowymi funkcjonalnościami Pythona """
result_of_multiplication = 1
for i in a:
    result_of_multiplication *= i
print(f"Result of multiplication: {result_of_multiplication}")


string = (str(result_of_multiplication))

sum_of_numbers = 0
for n in string:
    sum_of_numbers += int(n)
print(f"Sum of numbers in {result_of_multiplication}: {sum_of_numbers}")


from functools import reduce

"""Rozwiązanie inne"""
def multiply(x,y):
    return x*y


result = reduce(multiply, a)
print(result)

"""Wersja z lambdą"""
result1 = reduce(lambda x, y: x*y, a)
print(result1)

"""Wersja z lambdą"""
final_result = reduce(lambda x, y: x+y, [int(digit) for digit in str(result)])
print(final_result)

"""ekwiwalent jako sum"""
final_result1 = sum([int(digit) for digit in str(result)])
print(final_result1)

"""ekwiwalent z mapą"""
final_result2 = sum(map(int, str(result)))
print(final_result2)

""""GIGACHAD solution"""
print(sum(map(int, str(reduce(lambda x, y: x*y, a)))))