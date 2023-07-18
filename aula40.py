pessoa = {
    'nome':'Érico Toshiyuki',
    'sobrenome': 'Ide',
    'idade': '33 anos',
    'endereço': [
        {'rua': 'tal tal', 'número': 123},
    ]
}

print(pessoa['endereço'])

for chave in pessoa:
    print(chave, pessoa[chave])