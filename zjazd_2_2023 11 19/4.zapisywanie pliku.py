with open('textfile1.txt', 'w') as file:
    file.write('This is new text file.')

with open('textfile1.txt', 'a') as file:
    file.write('\n' 'Ala ma kota i psa.')