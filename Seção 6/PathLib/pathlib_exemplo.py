from pathlib import Path
from shutil import rmtree
caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

ideias = caminho_arquivo.parent.parent / 'ideias'
# print(ideias / 'arquivo.txt')

# LENDO DADOS DE UM ARQUIVO
# arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# arquivo.touch()
# print(arquivo)
# arquivo.write_text("Cuzinho")
# print(arquivo.read_text())
# arquivo.unlink()

# Escrevendo Dados dentro de um arquivo
# caminho_arquivo.touch()
# caminho_arquivo.write_text('')
# with caminho_arquivo.open('a+') as file:
#     file.write("Uma Linha\n")
#     file.write("outra Linha\n")
# print(caminho_arquivo.read_text())

caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text("Cufe")

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text("8FA")

# caminho_pasta.rmdir()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'files_{i}.txt'
    file.touch()

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write("Ola Mundi\n")
        text_file.write(f"file{i}.txt")

rmtree(caminho_pasta)