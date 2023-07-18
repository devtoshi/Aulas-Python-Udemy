entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Opss, você digitou alguma coisa errada')
    entrada = input('Você quer "entrar" ou "sair"? ')