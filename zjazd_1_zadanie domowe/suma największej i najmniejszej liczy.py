# zad 1: wyprintuj sumę największej i najmniejszej liczby w liście:
a = [2, 52, 5, 7, 12, 67, 22, 31]
# 1 sposób
a.sort()
number_1 = a[0]
number_2 = a[-1]
sum_of_numbers = number_1 + number_2
print(f"The smallest number is {number_1}")
print(f"The largest number is {number_2}")
print(f"The sum of these numbers is {sum_of_numbers}")

# 2 sposób
number_3 = min(a)
number_4 = max(a)
sum_of_number_1 = number_3 + number_4
print(f"The smallest number is {number_3}")
print(f"The largest number is {number_4}")
print(f"The sum od these numbers is {sum_of_number_1}")