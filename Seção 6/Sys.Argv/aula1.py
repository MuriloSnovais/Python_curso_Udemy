import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

print(qtd_argumentos)

if qtd_argumentos <= 1:
    print("Voce não passou argumentos")
else:
    print(f"Você passou os argumentos {argumentos[1:]}")