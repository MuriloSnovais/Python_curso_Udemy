import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.00},
    {'nome': 'Produto 3', 'preco': 15.00},
    {'nome': 'Produto 2', 'preco': 105.00},
    {'nome': 'Produto 4', 'preco': 69.90},
]


cont = 0 
for item in produtos:
    aumento = (item['preco'] * 10) / 100
    produtos[cont]['preco'] += aumento
    cont+= 1

def exibir(itens_dos_produtos):
    for item in itens_dos_produtos:
        print(item)
    print()
# Se fosse uma função ao inves do Lambda
#def mudar_ordem_nome_produtos_TRUEANDFALSE(x):
#    return x['nome']
#produtos_ordenados_decrescente = sorted(novos_produtos , key=mudar_ordem_nome_produtos_TRUEANDFALSE , reverse=True)

novos_produtos = copy.deepcopy(produtos)
produtos_ordenados_decrescente = sorted(novos_produtos , key=lambda x: x['nome'], reverse=True)
produtos_ordenados_por_nome = sorted(novos_produtos , key=lambda x: x['nome'], reverse=False).copy()
produtos_ordenados_por_preco_menor = sorted(novos_produtos , key=lambda x: x['preco'], reverse=False)
produtos_ordenados_por_preco_maior_copy = sorted(novos_produtos , key=lambda x: x['preco'], reverse=True).copy()

exibir(produtos_ordenados_decrescente)
exibir(produtos_ordenados_por_nome)
exibir(produtos_ordenados_por_preco_menor)
exibir(produtos_ordenados_por_preco_maior_copy)
print('PRODUTOS ORIGINAIS ABAIXO:')
for p in produtos:
    print(p)
    