# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo 
# deve ser contido dentro de uma única
# expressão.
# lista = [
#         {'nome': 'Luiz', 'sobrenome': 'miranda'},
#         {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#         {'nome': 'Daniel', 'sobrenome': 'Silva'},
#         {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#         {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [1, 43, 12 ,2 ,4 ,6 ,7,]

# print(lista)

# lista.sort()

# print(lista)

lista = [
        {'nome': 'Luiz', 'sobrenome': 'miranda'},
        {'nome': 'Maria', 'sobrenome': 'Oliveira'},
        {'nome': 'Daniel', 'sobrenome': 'Silva'},
        {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
        {'nome': 'Aline', 'sobrenome': 'Souza'},
]



lista.sort(key=lambda i: i['sobrenome'])

for item in lista:
    print(item)