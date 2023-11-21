#zadanie: uruchom ten algorytm dla liczb 2-100
#wyprintuj, której z liczba 2-100 zajęło najwięcej kroków by dotrzeć do 1

longest_path = 0
winning_number = 1
for number in range(2,101):
    collatz_path = [number]
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
            collatz_path.append(number)
    collatz_step_count = len(collatz_path) - 1
    if collatz_step_count > longest_path:
        longest_path = collatz_step_count
        winning_number = collatz_path[0]
print("The longest path is ",longest_path,"for number ", winning_number)



