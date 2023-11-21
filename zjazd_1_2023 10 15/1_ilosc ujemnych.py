numbers = [24, 12, 67, 3, -1, 67, -23, -78]
"""
for number in numbers:
    print(number)

i = 56
i += 1
"""
#policz i wyprintuj listy ujemne z listy

count = 0
for number in numbers:
    if number < 0:
        count += 1
print(count)

negative_numbers = [number for number in numbers if number <0]
print(len(negative_numbers))
"""
negative_numbers1 = [number-1 for number]
print(negative_numbers1)
"""
negative_numbers2 = [abs(number) for number in numbers if number < 0 ]
print(len(negative_numbers2))