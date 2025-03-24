"""
CPF: 033.766.640-72
10 9  8  7  6  5  4  3  2
0  3  3  7  6  6  6  4  0
0 27 24 49 36 30 24 12  0

soma = 202
202 * 10 = 
2020 % 11 = 

"""
import random
 
cpf_enviado_do_usuario = '03376664072'
nove_digitos = cpf_enviado_do_usuario[:9]
dez_digitos = cpf_enviado_do_usuario[:10]
contador_regressivo_1 = 10
contador_regressivo_2 = 11

resultado_digito_1 = 0
resultado_digito_2 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0 

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_do_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_do_usuario} é valido')
else:
    print('CPF não é valido')

    
