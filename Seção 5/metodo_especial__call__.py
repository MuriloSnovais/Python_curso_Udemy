# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

from typing import Any


class CallMe:
    def __init__(self,phone) -> None:
        self.phone = phone
    
    def __call__(self, nome,):
        print(nome , "está Chamando", self.phone)
        return 2134
    
call1 = CallMe("55+ 18 5981-6916")
retorno = call1('Muliru')
print(retorno)