# Peça 10 numeros, calcule e mostre os numeros pares e impares.
lista = []
lista_pares = []
lista_impares = []
for i in range(10):
    x = int(input('Digite um numero: '))
    lista.append(x)
    if x %2 == 0:
        lista_pares.append(x)

    else:
        lista_impares.append(x)
    
print(f'{lista_pares} essa lista é par')
print(f'{lista_impares} essa lista é par')