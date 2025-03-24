
nome = str(input("Digite seu Nome: "))
idade = (input("Digite sua Idade: "))
if nome and idade:
    print(f"Seu Nome é {nome}")
    print(f"Seu Nome Invertido é {nome[::-1]}")
    if ' ' in nome:
        print("Seu nome tem espaços")
    else:
        print("Seu nome não tem espaços")
    print(f"Seu nome tem {len(nome)} Letras")
    print(f"A primeira Letra do seu nome é {nome[0:1]}")
    print(f"A ultima letra do seu nome é {nome[-1:]}")  
else:
    print("Desculpe,você deixou campos vazios.")
