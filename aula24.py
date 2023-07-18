nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 1:
    print('Você digitou apenas um caractere, não caracteriza um nome')
elif tamanho_nome <= 4:
    print(f'Você digitou {nome} e possui {tamanho_nome} caracteres. Seu nome é curto')
elif tamanho_nome > 4 and tamanho_nome <= 6:
    print(f'Você digitou {nome} e possui {tamanho_nome} caracteres. Seu nome é normal')
else:
    print(f'Você digitou {nome} e possui {tamanho_nome} caracteres. Seu nome é muito grande')