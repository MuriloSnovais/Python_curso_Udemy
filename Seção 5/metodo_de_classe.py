
class Pessoa:
    ano = 2023 #atributo da classe

    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("OPA")

    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome, 50)
    
    @classmethod
    def anonimo(cls,idade):
        return cls("Anonima", idade)
    
p1 = Pessoa("Muliru",18)
p2 = Pessoa.criar_com_50_anos('João')
p3 = Pessoa("Anonima", 19)
p4 = Pessoa.anonimo(25)

print(p2.nome , p2.idade)
print(p3.nome , p3.idade)
print(p4.nome , p4.idade)
# Pessoa.metodo_de_classe()
