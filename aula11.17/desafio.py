# Peça a idade de 20 alunos. Faça um codigo que avisa quanto o aluno tem mais de 13 anos. 
aluno = 1
while aluno < 20:
    idade = int(input('Informe a sua idade: '))
    if idade > 13:
        print(f' A idade do aluno {aluno} é {idade}. É maior que 13.')
    aluno += 1
print('Fim da questão')

'''
while True:
    nota = int(input('Digite sua nota: '))
    if (nota < 0 or nota > 10):
        break'''

