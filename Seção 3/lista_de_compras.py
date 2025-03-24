import os
lista = []

while True:
    op = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ").lower()

    if op == 'i':
        compra = input("Adicione o Produta a lista: ")
        lista.append(compra)
    elif op == 'l':
        os.system('cls')
        print("Suas lista de Compras:")
        if lista == []:
            print("Não a nada na sua lista")
            continue
        for item in lista:
            print(f'{lista.index(item)} {item}')
    elif op == 's':
        print("Obrigado por Usar MuliruGroceryList")
        print(f"Estes foram seus itens da Lista:")
        print('=' * 30)
        if lista == []:
            print('Pobre...')
        for item in lista:
            print(f'{item}')
        print('=' * 30)
        break
    elif op == 'a':
        remover_compra = input("Que item deseja Remover?: ")
        try:
            remover_compra_int = int(remover_compra)
            del lista[remover_compra_int]
        except ValueError:
            print("Item não existe na lista")
        except IndexError:
            print("Digite um numero de um item da lista valido")
        except Exception:
            print("Erro desconhecido")
            