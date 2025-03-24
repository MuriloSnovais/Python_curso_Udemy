# def meu_repr(self):
#     class_name = self.__class__.__name__
#     class_dict = self.__dict__
#     class_repr = f'{class_name} ({class_dict})'
#     return class_repr

def adiociona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls

# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name} ({class_dict})'
#         return class_repr

@adiociona_repr
class Time:
    def __init__(self,nome) -> None:
        self.nome = nome
@adiociona_repr    
class Planeta:
    def __init__(self,nome) -> None:
        self.nome = nome

brasil = Time("Brasil")
portugual = Time("Portugual")
terra = Planeta("Terra")
marte = Planeta("Marte")

print(brasil)
print(portugual)

print(terra)
print(marte)