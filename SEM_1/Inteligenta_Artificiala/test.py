# Inițializarea variabilelor x și y
x = 3
y = 5

# Numărător pentru a ține evidența numărului de iterații
numar_iteratii = 0

# Repetă atribuirea până când x devine -27
while x != -27:
    x = 2 * x - y
    numar_iteratii += 1
    print(x, y)

print(numar_iteratii)
