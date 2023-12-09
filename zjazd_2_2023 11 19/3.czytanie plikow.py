with open('rozliczenie.csv', 'r') as plik1:
    content = plik1.readlines()
print(content)

for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[3])
print(content[3][2])

# obliczanie średniej wypłaty

total = 0
average = 0
for line in content[1:]:
    total += int(line[1])
average = round(total / len(content[1:]))
print(f"Średnia wypłata to: {average}")


count_maternity_leave = 0
for line in content[1:]:
    if line[3] == 'k' and line[4][0].lower() == 't':
        count_maternity_leave += 1
print(f"Liczba kobiet na macieżyńskim wynosi {count_maternity_leave}.")

with open ('C:\\Users\\adria\Desktop\\newfile.txt', 'a') as plik1:
    plik1.write('Kot i pies')
