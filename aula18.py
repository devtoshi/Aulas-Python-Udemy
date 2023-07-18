primeiro_valor = input('Digite o primeiro número: ')
segundo_valor = input('Digite o segundo número: ')

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)

a = primeiro_valor_int
b = segundo_valor_int

if a > b:
    print('O número {} é maior que {}'.format(a,b))
elif a < b:
    print('O número {} é menor que {}'.format(a,b))
else:
    print('O número {} é igual a {}'.format(a,b))