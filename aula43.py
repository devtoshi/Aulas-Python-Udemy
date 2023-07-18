pessoa = {
    'nome': 'Érico',
    'sobrenome': 'Ide',
    'idade': '33 anos',
}

# n1 = pessoa.get('nome')
# n2 = pessoa.get('rua', 'Não existe')
# nome = pessoa.pop('nome')


# print(n1)
# print(n2)
# print(nome)
# print(pessoa)

pessoa.update({
    'rua': 'Rua Tal Tal'
})

print(pessoa)