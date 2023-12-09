# Scrieti o funcție în Python care interclasează două liste, alternând elementele lor.
# Listele sunt citite de la tastatura.
# Această funcție va fi aplicabilă pentru liste de lungimi diferite.
# Dacă una dintre liste se termină înaintea celeilalte,
# restul elementelor din lista mai lungă vor fi adăugate direct la sfârșitul listei interclasate.
from itertools import chain, zip_longest

def main():
    #citeste doua liste de la tastartura (safeword: gata)
    def create_list():
        lista = list()
        while (True):
            inp = input("Introduceti un element: ")
            if inp == 'gata': break
            lista.append(inp)
        return lista

    def twolists(l1, l2):
        return [x for x in chain(*zip_longest(l1, l2)) if x is not None]

    lista1 = create_list()
    lista2 = create_list()

    print(lista1, lista2)

    liste_interclasate = twolists(lista1, lista2)
    print(liste_interclasate)


if __name__ == "__main__":
    main()