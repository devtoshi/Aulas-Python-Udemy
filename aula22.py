entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    if entrada_int % 2 == 0:
        print(f'O número {entrada_int} é par')
    else:
        print(f'O número {entrada_int} é impar')
else:
    print('Você não digitou um número inteiro')