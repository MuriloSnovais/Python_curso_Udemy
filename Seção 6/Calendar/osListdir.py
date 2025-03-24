# \Users\Muliru\Desktop\aulas programação\aulas programação\Python curso Udemy\seção 6
# caminho = r'\\Users\Muliru\\Desktop\\aulas programação\\aulas programação\\Python curso Udemy\\seção 6'
import os
caminho = os.path.join('Users','Muliru','Desktop','aulas programação','Python curso Udemy','seção 6' )
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)

