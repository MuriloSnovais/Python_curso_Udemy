class Animal:
    def __init__(self,nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def Comendo(self,alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self,*args,**kwargs):
        return self.Comendo(*args,**kwargs)
    
leao = Animal("Leão")
print(leao.nome)
print(leao.executar("Carne"))