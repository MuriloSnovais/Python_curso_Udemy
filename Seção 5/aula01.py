class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Murilo' , 'Santana')
# p1.nome = 'Murilo'
# p1.sobrenome = 'Santana'

p2 = Pessoa("Ygor", "Santana")
# p2.nome = 'Ygor'
# p2.sobrenome = 'Novais'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)