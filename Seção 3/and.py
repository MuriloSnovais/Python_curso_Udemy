# Enteder como funciona o AND

entrada = input("[E]ntrar [S]air: ").upper()
senha_Digitada = input("Senha: ") 

senha_Permitida = '1234'

if entrada == "E" and senha_Digitada == senha_Permitida:
    print("Entrou")
else:
    print("Saiu")

