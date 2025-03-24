import os
palavra_secreta = "laranja"
palavra_formada = ''
cont = 0

while True:
    #Para a pessoa digitar a letra
    letra_digitada = str(input("Digite uma letra: "))
    cont += 1

    #saber se digitou apenas uma letra
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra seu Burro...")
        continue

    #se a letra digitada está na palavra secreta
    if letra_digitada in palavra_secreta:
        palavra_formada += letra_digitada
    
    # para analisar cada letra com um FOR e saber se ela está na palavra secreta
    palavra_escrita = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavra_formada:
            palavra_escrita += letra_secreta
        else:
            palavra_escrita += '*'
    

    print(f"A palavra Formada {palavra_escrita}")

    if palavra_escrita == palavra_secreta:
        os.system('cls')
        print("Você GANHOU Congratulations my FRIEND!!! ")
        print(f"A palavra era {palavra_secreta}")
        print(f"Tentativas: {cont}x")
        break
        
        




    
    
    


