class Caneta:
    def __init__(self,cor):
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print("ESTOU NO GETTER")
        return self._cor
    
    @cor.setter
    def cor(self,valor):
        # if valor == 'Preto':
        #     raise ValueError("Não gosto de Preto")
        print('ESTOU NO SETTER')
        self._cor = valor
 
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self,valor):
        self._cor_tampa = valor



caneta = Caneta("Azul")
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)
