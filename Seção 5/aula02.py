class Carro:
    def __init__(self,nome='Sei Lá'):
        self.nome = nome 

    def acelerar(self):
        print(f"{self.nome} Está acelerando...VRUUMMMMMMMMMMMM")

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta') 
print(celta.nome)
celta.acelerar()        