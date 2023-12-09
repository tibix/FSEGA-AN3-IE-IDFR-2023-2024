# Realizati un program care calculeaza distributia emailurilor din fisierul mbox-short.txt in functie de ora,
# pentru fiecare mesaj transmis. Ora poate fi extrasa din linia ce incepe cu “From” prin identificarea sirului
# de caractere ce contine ora si apoi impartirea lui folosind caracterul “:”. Dupa ce ati numarat emailurile
# pe fiecare ora, afisati numarul lor sortat in functie de ora, asa cum arata in exemplul de mai jos:

with open('mbox-short.txt') as f:
    lines = [line for line in f if line.startswith("From") and len(line.split(' ')) > 4]

mails_per_hour = dict()
for line in lines:
    words = line.split(' ')
    ora = words[6].split(':')[0]
    mails_per_hour[ora] = mails_per_hour.get(ora, 0)+1

sorted_mails_per_hour = list(mails_per_hour.items())
sorted_mails_per_hour.sort()

for item in sorted_mails_per_hour:
    print(item[0], item[1])

# sorted_mails_per_hour = {i: mails_per_hour[i] for i in dict_keys}
# for key, value in sorted_mails_per_hour.items():
#     print(key, value)

