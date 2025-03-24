from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'EndereçosNomes.csv'
print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['Nome'])

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)
#     # next(leitor)
#     # print(next(leitor))
#     for linha in leitor:
#         print(linha[0])