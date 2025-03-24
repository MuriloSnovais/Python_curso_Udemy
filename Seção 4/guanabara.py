valor = []
for n in range(0,5):
    numero = int(input(f"Digite um valor para a posição {n}: "))
    valor.append(numero)

maior_valor = max(valor)
menor_valor = min(valor)
print('-=-' * 15)
print(f"Você digitou os valores {valor}")
print(f"O maior valor digitado foi {maior_valor} nas posições {valor.index(maior_valor)}")
print(f"O menor valor digitado foi {menor_valor} nas posições {valor.index(menor_valor)}")