lista_a = [1234, 'Érico', True, 'abc1']
lista_a.append('Mariana')

indices = range(len(lista_a))

print(indices)

for indice in indices:
    print(indice, lista_a[indice], type(lista_a[indice]))

    