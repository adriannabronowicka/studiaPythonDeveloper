from more_itertools import first

def get_2_digit_number_flex(string: str) -> int:
    digit_1 = first(char for char in string if char.isdigit())
    digit_2 = first(char for char in reversed(string) if char.isdigit())
    return int(digit_1 + digit_2)


with open('advent_2.txt', 'r') as file1:
    content = file1.readlines()

list_of_number = []
for i in content:
    list_of_number.append(get_2_digit_number_flex(i))
print(sum(list_of_number))

"""kolejne rozwiązanie"""
lines = open('advent_2.txt').readlines()
result = sum(get_2_digit_number_flex(line) for line in lines)
print(result)

""""kolejne rozwiązanie"""
result1 = sum(map(get_2_digit_number_flex, lines))
print(result1)

