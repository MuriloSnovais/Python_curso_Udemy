# class MinhaString(str):
#     def upper(self):
#         print("Chamou Upper")
#         retorno = super().upper()
#         print("Depois do Upper")
#         return retorno


# string = MinhaString("Muliru")
# print(string.upper())

class A:
    atributo_a = 'manteiga'
    def __init__(self,atributo):
        self.atributo = atributo

    def metodo(self):
        print("A")

class B(A):
    atributo_b = 'no'

    def __init__(self, atributo,outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print("B")

class C(B):
    atributo_c = 'pão'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print('Burlei o Sistema.')
    
    def metodo(self):
        super().metodo() # B
        super(B,self).metodo() # A
        print("C")

# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('atributo', 'qualquer')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()

