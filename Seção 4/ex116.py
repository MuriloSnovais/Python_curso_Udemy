caminho_arquivo = 'aula116.txt'

with open(caminho_arquivo, 'w+' , encoding='UTF-8') as arquivo:
    arquivo.write('ATENÇÃO\n')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'Linha 4\n') 
    )
    arquivo.seek(0,0)
    print(arquivo.read())
    print("Lendo")
    arquivo.seek(0,0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print("READLINES")
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('-=-' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

