"""wyprintuj date, któa była 10 tys dni temu"""

from datetime import datetime, timedelta

date_now = datetime.now().date()
date = date_now - timedelta(days=10000)
print(date)

"""Liczba numerologiczna"""
date_number = (str(date)).replace("-", "")

numbers = []

for number in date_number:
    numbers.append(int(number))
print(numbers)

sum_of_numbers = sum(numbers)
print(sum_of_numbers)


while sum_of_numbers > 9:
    sum_of_numbers = str(sum_of_numbers)
    list_of_numbers = [int(i) for i in sum_of_numbers]
    sum_of_numbers = sum(list_of_numbers)
    list_of_numbers.clear()

print(sum_of_numbers)


"""def get_digit_sum(number: int) -> int:
    if sum_of_numbers < 9:
        return sum_of_numbers
    else:
        digit_sum = sum(map(int, list(str(sum_of_numbers))))
        return get_digit_sum(digit_sum)


print(get_digit_sum(19920215))"""   #coś tu nie działa, sprawdzić na github w repo później
