# Scrieți un program care deschide fișierul romeo.txt și îl citește linie cu linie.
# Pentru fiecare linie, separati linia într-o listă de cuvinte folosind funcția split.
# Extrageți într-o altă listă cuvinte, astfel încât acestea să
# nu se repete (Verificați fiecare cuvânt daca este intr-o listă, iar dacă nu apare, adăugați-l).
# Când programul se termină, sortați și printați cuvintele din listă în ordine alfabetică



with open('romeo.txt', 'r') as file:
    lines = file.readlines()

words = []
for line in lines:
    wordline = line.split(' ')
    # print(wordline)
    for word in wordline:
        if word not in words:
            words.append(word)

for word in words:
    if word.endswith('\n'):
        words.remove(word)
        word = word.strip('\n')
        words.append(word)
sorted_words = sorted(words)
print(sorted_words)