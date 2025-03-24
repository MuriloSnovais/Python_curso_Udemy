def contar_bits_um(numero):
    # Converte o número para a representação binária e conta os '1's
    return bin(numero).count('1')

numero = int(input("Insert a number: "))
# Exemplo de uso:
resultado = contar_bits_um(numero)
print(f"O número de bits igual a 1 em {numero} é: {resultado}")
