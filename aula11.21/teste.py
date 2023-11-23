# Peça 10 numeros inteiros, calcule e mostre os numeros pares e impares.
'''contador_par = 0
contador_impar = 0
for i in range(1,11):
    numeros = int(input("Digite um numero: "))
    if numeros % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1
print(f'A quantidade de numeros pares é {contador_par}')
print(f'A quantidade de numeros pares é {contador_impar}')'''

# Faça um programa que dado um conjunto de N numeros, determine o menor valor, o maior valor e a soma dos valores
'''maior = 0
menor = None # É nada
while True:
    saida = input(" Digite 'S' para sair: ") 
    if saida == 's' or saida == 'S':
        print('Você saiu!')
        break 
    numero = int(input('Informe um numero inteiro: '))
    if numero > maior:
        maior = numero
    if menor == None or numero < menor:
        menor = numero
print(f' A soma de {maior} + {menor} = {maior+menor}')
print(f'O maior é {maior}')
print(f'O mneor é {menor}')'''

# Faça um programa que peça um numero inteiro e determine se ele é ou não um numero primo.
# 1 2 3 4 5 6 7 8 9 10 11

'''numero = int(input('Informe um numero inteiro: '))
intervalo = range(1, numero+1)
contador = 0
for i in intervalo:
    if numero % i == 0:
        print(f'Foi dividivel por {i}')
        contador += 1
if contador == 2:
    print(f'O numero {numero} é primo') 
else:
    print(f' o numero {numero} não é primo')'''


# Faça um programa que peça a idade de 10 pessoas. Ao final do programa
contador = 0
for i in range(10):
    idade = int(input('Informe sua idade: '))
    contador+= idade
    media = contador/10
print(media)
    