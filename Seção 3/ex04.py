nome = str(input("Digite seu primeiro nome: "))

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) <= 6:
    print("Seu nome é Normal")
else:
    print("Seu Nome é grande pra caralho!")