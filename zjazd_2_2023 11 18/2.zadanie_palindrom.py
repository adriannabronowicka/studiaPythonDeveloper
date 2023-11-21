#Program sprawdzi czy dane słowo lub zdanie jest palindromem

list_of_sentences =[]
sentence = input("Podaj wyrazenie: ")
list_of_sentences.append(sentence)
max_length = len(sentence)
while True:
    print(sentence)
    new_sentence = sentence.replace(" ","")
    new_sentence = sentence.replace(".","")
    new_sentence = sentence.replace(",","")
    if new_sentence.lower() == new_sentence.lower()[::-1]:
        print("To jest palindrom")
    else:
        print("To nie jest palindrom")

    decision = input("Czy chcesz sprawdzić kolejne słowo. Wpisz tak czy nie. ")
    if decision == "tak":
        sentence = input('Podaj kolejne wyrazenie: ')
        list_of_sentences.append(sentence)
        if len(sentence) > max_length:
            max_length = len(sentence)
    else:
        break

print(f'statystyki:')
print(f'liczba sprawdzonych slow: {len(list_of_sentences)},\nnajdlusze ma: {max_length} znakow')



