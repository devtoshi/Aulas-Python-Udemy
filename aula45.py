# add, update, discard
s1 = set()

s1.add('Érico')
s1.add(1)
s1.update(('Olá, Mundo!', 1, 2, 3, 4))
s1.discard('Olá, Mundo!')

print(s1)