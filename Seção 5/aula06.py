class Pessoa:
    ano_atual = 2024

    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa("Murilo" , 18)
# p1.nome = 'EITA'
# del p1.nome
# print(p1.idade)
print(p1.__dict__)
print(vars(p1))