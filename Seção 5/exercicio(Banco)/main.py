import contas
import pessoas

c1 = pessoas.Cliente('Murilo', 18)
cc1 = contas.ContaCorrente(111, 222, 0, 0)
c1.conta = cc1
c2 = pessoas.Cliente('Ygor', 24)
cp1 = contas.ContaPoupanca(112, 223, 100)
c2.conta = cp1


cc1.deposito(1000)
cc1.sacar(151)
cp1.deposito(150)
cp1.sacar(59)

