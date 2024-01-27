"""
1. Znajdź pierwszą cyfrę od lewej i od prawej z zadanego napisu
2. Połącz znalezione 2 cyfry w liczbę 2-cyfrową
"""

from more_itertools import first
string = "oinj3odbifh5oiugbdfn4865nv"


def create_number(string1):
    for l in string1:
        if l.isdigit():
            print(f"First digit from left {l}")
            break
    for k in string1[::-1]:
        if k.isdigit():
            print(f"First digit from right {k}")
            break
    return(f"Number: {str(l) + str(k)}")


print(create_number(string))

def get_2_digit_number_flex(string2: str) -> int:
    digit_1 = first(char for char in string2 if char.isdigit())
    digit_2 = first(char for char in reversed(string2) if char.isdigit())
    return int(digit_1 + digit_2)

print(get_2_digit_number_flex(string))
