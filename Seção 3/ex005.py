nome = str(input('Digite um nome: '))
indice = 0
novo_nome = ''
caractere = input('Digite uma caractere: ')
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{caractere}{letra}'
    indice += 1
        

print(novo_nome)