def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name} ({class_dict})'
    return class_repr

def adiociona_repr(cls):
    cls.__repr__ = meu_repr
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'Terra' in resultado:
            return 'Você esta em Casa'
        return resultado
    return interno

@adiociona_repr
class Time:
    def __init__(self,nome) -> None:
        self.nome = nome

@adiociona_repr    
class Planeta:
    def __init__(self,nome) -> None:
        self.nome = nome
    
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'

brasil = Time("Brasil")
portugual = Time("Portugual")
terra = Planeta("Terra")
marte = Planeta("Marte")

print(brasil)
print(portugual)

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())