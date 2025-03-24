questions = [
    {
        'Pergunta': 'Quanto é 5+5?',
        'Opções': ['15' , '10' , '4' , '910'],
        'Resposta': '10',
    },
    {
        'Pergunta': 'Quanto é 2x1000?',
        'Opções': ['2000' , '2' , '4' , '1600'],
        'Resposta': '2000',
    },
    {
        'Pergunta': 'Quanto é 75x2?',
        'Opções': ['160' , '144' , '30' , '150'],
        'Resposta': '150',
    },
]

cont = 0
for question in questions:
    options = question['Opções']
    print(f'Question: {question['Pergunta']}')
    print('alternatives: ')
    for n,alternates in enumerate(options):
        print(f'{n}) {alternates}')

    got = False
    choice = input("Choice a alternative: ")
    choice_int = None
    qtd_options = len(options)

    if choice.isdigit():
        choice_int = int(choice)
    
    if choice_int is not None:
        if choice_int >= 0 and choice_int < qtd_options:
            if options[choice_int] == question['Resposta']:
                cont += 1
                got = True
                
    if got:
        print("NICE 😀")
    else:
        print("WRONG 😡")
print(f"Correct answers: {cont}")
    
