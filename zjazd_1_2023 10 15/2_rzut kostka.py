#oblicz eksperymentalnie prawdpopodobienstwo
#wyrzucenia conajmniej 1 szóstki rzutem trzema kostkami

import random

total_rolls = 100
counter_6 = 0

for i in range(total_rolls):
    for _ in range(3):
        if random.randint(1,6) == 6:
            counter_6 += 1
print("six rolled", counter_6," times")

probability = counter_6/ total_rolls * 100
print("Probability is:", probability, "%")