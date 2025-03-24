# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Escritor:
    def __init__(self,nome):
        self.nome = nome
        self._ferramenta = None
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self,nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo'
    
escritor = Escritor("Muliru")
caneta = FerramentaDeEscrever("Caneta")
maquina_de_escrever = FerramentaDeEscrever("Maquina")
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())
    
 