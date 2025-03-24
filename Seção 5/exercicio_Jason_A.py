import json

CAMINHO_ARQUIVO = 'exercicio_Jason_A.json'
class Dados:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    

p1 = Dados("Murilo" , 18)
p2 = Dados("Ygor" , 24)
p3 = Dados("Robertin" , 32)

bd = [vars(p1),vars(p2),vars(p3)]

with open(CAMINHO_ARQUIVO , 'w') as arquivo:
    json.dump(bd, arquivo,ensure_ascii=False,indent=2)