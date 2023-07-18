for i in range(10):
    if i == 2:
        print('o i é igual a 2, pulando')
        continue

    if i == 8:
        print('i é igual a 8, seu else não será executado')
        break

    for j in range(1,3):
        print(i,j)

else:
    print('For completo com')