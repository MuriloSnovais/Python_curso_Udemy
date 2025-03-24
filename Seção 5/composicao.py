class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self,rua,numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self,rua,numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print("APAGANDO", self.rua, self.numero)

cliente1 = Cliente("Murilo")
cliente1.inserir_endereco("Martins frança", 517)
cliente1.inserir_endereco("Cara cacaf", 151)
cliente1.listar_enderecos()

print("AQUI TERMINA MEU CODIGO")
