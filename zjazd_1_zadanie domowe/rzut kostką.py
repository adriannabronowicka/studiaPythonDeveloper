#  Oblicz (eksperymentalnie) prawdopodobieństwo wyrzucenia min. 1 szóstki
#  rzutem 3 kostkami k6

import random

count = 0
success_count = 0
total_rolls = 100

for i in range(total_rolls):
    for j in range(3):
        if random.randint(1,6) == 6:
            count += 1
    if count != 0:
        success_count += 1
    count = 0

probability = success_count / total_rolls * 100
print(f"The number of success {success_count}")
print(f"Probability of rolling 6 is {probability}")


"""
success_count1 = 0

for i in range(total_rolls):
    success_count1 += any([random.randint(1,6) == 6 for j in range(3)])

probability = success_count1 / total_rolls *100
print(f"The number of success {success_count1}")
print(f"Probability is {probability} ")
"""