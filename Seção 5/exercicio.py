class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor
    

class Motor:
    def __init__(self,nome):
        self.nome = nome

class Fabricante:
    def __init__(self,nome):
        self.nome = nome

carro1 = Carro("Fusca")
motor1 = Motor("CB-250")
fabricante1 = Fabricante("Chevrolet")
carro1.fabricante = fabricante1
carro1.motor = motor1
print(f'O carro {carro1.nome} pertence a fabricante {carro1.fabricante.nome} com o motor {carro1.motor.nome}.')

