import json
from exercicio_Jason_A import CAMINHO_ARQUIVO,Dados

with open(CAMINHO_ARQUIVO, 'r' , encoding='utf8') as arquivo:
    dados = json.load(arquivo)

    p1 = Dados(**dados[0])
    p2 = Dados(**dados[1])
    p3 = Dados(**dados[2])

    print(p1.nome , p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)