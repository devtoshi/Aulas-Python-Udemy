import os
itens_adicionados = []
item_inserido = []
while True:
    print('Escolha uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')
    
    if opcao == 'i':
        os.system('cls')
        item = input('Digite o item a ser adicionado na lista: ')
        itens_adicionados.append(item)

    elif opcao == 'a':
        item_del = input('Escolha o indice que deseja apagar: ')
        try:
            indice_int = int(item_del)
            del itens_adicionados[indice_int]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Por favor digite um indice da lista')

    elif opcao == 'l':
        os.system('cls')
        for indice, produto in enumerate(itens_adicionados):
            print(indice, produto)
    
    else:
        print('Você digitou uma opção não listada')