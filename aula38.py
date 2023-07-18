def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total


a = multiplicar(1,2,3,4,5)
print(a)


def par_impar(numero):
    multiplo_dois = numero % 2 == 0

    if multiplo_dois:
        return f'{numero} é par'
    
    return f'{numero} é impar'
    
print(par_impar(5))
print(par_impar(10))
print(par_impar(15))