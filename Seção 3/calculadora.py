n1 = float(input("Digite um numero: "))
n2 = float(input("Digite mais um numero: "))
escolha = ''
op = 0
while True:
    print(" [1] ADIÇÃO \n [2] SUBTRAÇÃO \n [3] MULTIPLICAÇÃO \n [4] DIVISÃO")
    op = float(input("Escolha uma opção: "))
    if op == 1:
        print(f'Seu Resultado foi {n1+n2}')
        escolha = str(input("Deseja continuar?: ")).upper()
        if escolha == 'SIM':
            n1 = float(input("Digite um numero: "))
            n2 = float(input("Digite mais um numero: "))
        elif escolha == 'NAO' or "NÃO":
            break
    if op == 2:
        print(f'Seu Resultado foi {n1-n2}')
        escolha = str(input("Deseja continuar?: ")).upper()
        if escolha == 'SIM':
            n1 = float(input("Digite um numero: "))
            n2 = float(input("Digite mais um numero: "))
        elif escolha == 'NAO' or "NÃO":
            break
    if op == 3:
        print(f'Seu Resultado foi {n1*n2}')
        escolha = str(input("Deseja continuar?: ")).upper()
        if escolha == 'SIM':
            n1 = float(input("Digite um numero: "))
            n2 = float(input("Digite mais um numero: "))
        elif escolha == 'NAO' or "NÃO":
            break
    if op == 4:
        print(f'Seu Resultado foi {n1/n2:.2f}')
        escolha = str(input("Deseja continuar?: ")).upper()
        if escolha == 'SIM':
            n1 = float(input("Digite um numero: "))
            n2 = float(input("Digite mais um numero: "))
        elif escolha == 'NAO' or "NÃO":
            break
    elif op > 4:
        print("Digite uma opção valida")

print("Obrigado por utilizar Muliru's Calculator")