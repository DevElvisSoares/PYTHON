# 1.0 Faça um quiz utilizando um dicionario com as seguintes chaves: perguntas, opções e respostas. Faça a validação da opção escolhida com a resposta e imprima.


dic_perguntas = [{'Pergunta': 'Quem decobriu o Brasil? ', 'Opções':['Lula', 'Bolsonaro', 'Cristovão Colombo', 'Cabral'], 'Resposta': 'Cabral' }, 
                 
                 {'Pergunta': 'Quem foi o presidente do Brasil na pandemia? ', 'Opções':['Lula', 'Bolsonaro', 'Cristovão Colombo', 'Pedro Alvares Cabral'], 'Resposta': 'Bolsonaro' },
                 
                 {'Pergunta': 'Quem é o atual presidente do Brasil? ', 'Opções':['Lula', 'Bolsonaro', 'Cristovão Colombo', 'Pedro Alvares Cabral'], 'Resposta': 'Lula' }]
                 
                 



for pergunta in dic_perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    #pergunta = input(dic_perguntas['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i+1})', opcao)
        print()

    escolha = input('Escolha sua opção: ')
    acertou = False
    if escolha == pergunta['Resposta']:
        acertou = True
    if acertou:
        print('Você acertou 👍')
        print()
    else: 
        print('Você errou 😞')
        print()
    

     



