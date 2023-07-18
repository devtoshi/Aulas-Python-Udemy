def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(numero)
    print(total)


soma(1,2,3,4,5)

