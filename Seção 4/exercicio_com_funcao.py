def multiplacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
def par_impar(*args):
    for numero in args:
        if numero % 2 == 0:
            return f'{numero} é par'
        return f'{numero} é impar'



multiplicar = multiplacao(1,2,3,4,5)
print(multiplicar)
print(par_impar(1))
print(par_impar(6))
print(par_impar(4))
print(par_impar(7))
