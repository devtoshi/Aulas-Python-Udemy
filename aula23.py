horas = input('Digite que horas são: ')

if horas.isdigit():
    horas_int = int(horas)
    if horas_int >= 0 and horas_int <= 11:
        print(f'Você digitou {horas_int} horas, Bom dia!')
    elif horas_int > 11 and horas_int <= 17:
        print(f'Você digitou {horas_int} horas, Boa tarde!')
    else:
        print(f'Você digitou {horas_int} horas, Boa noite!')
else:
    print('Você não digitou um número')