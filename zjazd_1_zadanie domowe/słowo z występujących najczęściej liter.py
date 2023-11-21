# zad 6: wyprintuj 4 najczęściej występujące litery w zmiennej 'b' jako 4-literowe słowo
b = "pip! dwudziestu uzurpatorow dusi padalcem dwa pudle"

list = [letter
        for letter in b
        if letter != " " and letter != "!"]
word =[]
number_of_letter = 4

for i in range(number_of_letter):
    max_letter = max(list, key = list.count )
    word.append(max_letter)
    while max_letter in list:
        list.remove(max_letter)
print(''.join(word))

#inny sposób zapisu słowa
print(word[0] + word[1] + word[2] + word[3])
