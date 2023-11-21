import random
total_rolls = 1000
success_count = 0
for i in range(total_rolls):
    roll_result = [random.randint(1,6) for _ in range(3)]
    success_count += any([i == 6 for i in roll_result])

probability = success_count/ total_rolls * 100
print("Probability is:", probability, "%")