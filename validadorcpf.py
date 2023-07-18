import os
while True:
    cpf_digitado = input('Digito o número do CPF: ')
    nove_digitos = cpf_digitado[:9]
    contador_regressivo_1 = 10
    contador_regressivo_2 = 11
    nono_digito = str(cpf_digitado)

    resultado_digito_1 = 0
    for digito in nove_digitos:
    
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0


    dez_digitos = nove_digitos + str(digito_1)

    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_digitado == cpf_gerado:
        print (f'O CPF:{cpf_digitado} é Válido')
        if nono_digito[8] == '8':
            print ('Seu CPF é de SP')
        elif nono_digito[8] == '1':
            print ('Seu CPF é do DF, GO, MS, MT ou TO')
        elif nono_digito[8] == '4':
            print ('Seu CPF é de AL, PB, PE ou RN')
        elif nono_digito[8] == '3':
            print ('Seu CPF é do CE, MA ou PI')
        elif nono_digito[8] == '2':
            print ('Seu CPF é do AC, AM, AP, PA, RO ou RR')
        elif nono_digito[8] == '5':
            print ('Seu CPF é da BA ou SE')
        elif nono_digito[8] == '6':
            print('Seu CPF é de MG')
        elif nono_digito[8] == '7':
            print('Seu CPF é do ES ou RJ')
        elif nono_digito[8] == '9':
            print('Seu CPF é do PR ou SC')
        else:
            print('Seu CPF é do RS')
    else:
        print('CPF Inválido')
    print('Deseja validar outro CPF?')

    resposta = input('[s]im ou [n]ão: ')

    if resposta == 's':
        os.system('cls')
        continue

    elif resposta == 'n':
        os.system('cls')
        print('Saindo...')
        break
    

