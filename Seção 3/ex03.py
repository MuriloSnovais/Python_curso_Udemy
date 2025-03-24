entrada = input("Digite que horas são agora: ")
try:
    horario = int(entrada) 
    if horario <= 11:
        print("Bom Dia")
    elif horario <= 17 :
        print("Boa Tarde")
    elif horario <= 23:
        print("Boa noite")
    else:
        print("Não reconheco o horario porra")

except:
    print("Por favor, Digite apenas numeros inteiros")
