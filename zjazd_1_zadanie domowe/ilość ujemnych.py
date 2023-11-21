numbers = [24, 12, 67, 3, -1, 67, -23, -78]

# policz liczby ujemne z listy powyżej. Wyprintuj ich ilość.
#1 sposób
negative_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(number)
print(f"Negative numbers are: {negative_numbers}")
print(f"Amount of negative numbers is: {len(negative_numbers)}")

#2 sposób z list comprehension
negative_numbers1 = [number
                     for number in numbers
                     if number < 0]
print(f"Negative numbers are{negative_numbers1}")
print(f"Amount of negative numbers is {len(negative_numbers1)}")