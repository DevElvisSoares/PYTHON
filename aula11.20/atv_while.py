
'''while True:
    nota = int(input("Digite uma nota de 0 a 10: "))
    if nota < 0 or nota > 10:
        print('Essa nota é invalida')
    if nota >= 0 and nota <=10:
        break'''

'''while True:
    nome = input('Digite seu nome: ')
    senha = (input('Digite sua senha:'))
    if nome == senha:
        print('Erro. Sua senha não pode ser igual ao nome do usuario. Digite novamente')
    if nome != senha:
        break'''
tentativa = 1
num1 = 0
while tentativa <= 5:
    num = int(input('Digite um numero: '))
    if num > num1:
        num1 = num
    tentativa += 1
print(f'O maior numero é {num1}')
