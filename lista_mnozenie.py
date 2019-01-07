lista = [1.5, 4.5, 1, 2, 2]

n = None
for i in lista:
    if n is None:
        n = i
    else:
        n *= i

print (n)
