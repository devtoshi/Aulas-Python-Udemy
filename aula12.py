nome = input("Digite o seu nome: ")
altura = input("Digite a sua altura: ")
massa = input("Digite o sua massa: ")

imc = (float(massa)) / (float(altura)**(2))

print("Seu nome é: ",nome)
print("Sua altura é: ", altura)
print("Sua massa é: ", massa)

linha_1 = f'{nome} seu imc é {imc:.2f} e você está acima do peso'
linha_2 = f'{nome} seu imc é {imc:.2f} e você não está acima do peso'
if imc >= 25:
    print(linha_1)
else:
    print(linha_2)

