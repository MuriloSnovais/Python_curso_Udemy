from abc import ABC, abstractmethod

class Contas(ABC):
    def __init__(self,agencia: int,conta: int,saldo: float=0) -> None:
        super().__init__()
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self,valor: float) -> float :...

    def deposito(self,valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor})')
        return self.saldo
    
    def detalhes(self,msg: str='') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('-=-')
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name} {attrs}'


class ContaPoupanca(Contas):
    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        print("Não foi possivel sacar o valor desejado")
        self.detalhes(f"(SAQUE NEGADO R${valor})")
        return self.saldo

class ContaCorrente(Contas):
    def __init__(self,agencia: int,conta:int,saldo:float =0,limite:float=0) -> None:
        super().__init__(agencia,conta,saldo)
        self.limite = limite

    def sacar(self,valor:float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print("Não foi possivel sacar o valor desejado")
        print(f"Seu Limite é {-self.limite:.2f}")
        self.detalhes(f"(SAQUE NEGADO R${valor})")
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name} {attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111,222)
    cp1.sacar(1)
    cp1.deposito(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')

    cc1 = ContaCorrente(111,222,0, 100)
    cc1.sacar(1)
    cc1.deposito(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(2)
    print('##')