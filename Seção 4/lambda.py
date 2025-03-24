
def executa(valor, *args):
    return valor(*args)


print(executa(lambda x,y: x + y, 2 , 5))