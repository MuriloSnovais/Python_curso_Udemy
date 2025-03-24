# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(x,y):
    juntar = zip(x,y)
    for i in juntar:
        print(i)
    

list_City = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_Region = ['BA', 'SP', 'MG', 'RJ']

zipper(list_City,list_Region)




