class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = "Isso é Privado"
    
    def metodo_publico(self):
        print(self.__private)
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return "_metodo_protected"

    def _metodo__private(self):
        return "__metodo__privado"
    

f = Foo()
print(f._metodo__private())
# print(f._protected)
# print(f._metodo_protected())
# print(f.public)
# print(f.metodo_publico())