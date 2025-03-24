def adicionar_item_lista():
    tarefas = str(input('Adicione sua Tarefa: '))
    return lista.append(tarefas)


lista = []
lista_backup = []
refazer_lista = []
    
print("Comandos: adicionar,listar, desfazer, refazer, sair")
while True:
    comando = str(input("Digite uma tarefa ou comando: ")).lower()
    if comando == 'adicionar':
        adicionar_item_lista()
        print('TAREFAS: ')
        for item in lista:
            print(item)
    elif comando == 'listar':
        print("SUA LISTA COMPLETA:")
        for item in lista:
            print(item)
    elif comando == 'desfazer':
        lista_backup = lista.pop()
        refazer_lista.append(lista_backup)
        print(f'item: {lista_backup} removido da lista')
    elif comando == 'refazer':
        lista_backup = refazer_lista.pop()
        print(f'item: {lista_backup} adicionado devolta a lista')
        lista.append(lista_backup)
    elif comando == 'sair':
        break
    else:
        print("Você digitou algo errado")





