import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'CSVWRITER.csv'

lista_clientes = [
    {'Nome': 'Muliru' , 'Endereco': 'AV 1, AV2'},
    {'Nome': 'Ygor' , 'Endereco': 'R 1, R 2'},
    {'Nome': 'Mauro' , 'Endereco': 'CU 1, CU 2'}
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo,fieldnames=nome_colunas)
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)


# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())


