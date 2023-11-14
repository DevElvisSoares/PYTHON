# Listas são um conjuto de elementos

lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

# O sinal de + soma numeros e concatena strings

a = 2
b = 3

c = 'Amo' 
d = 'Valley'

print(c + d)
print(a + b)
lista_c = lista_a + lista_b
print(lista_c , type(lista_c))


# Polimorfismo : é a capacidade de alguma coisa ser utilizada de varias formas em varias situações

lista_a.extend(lista_b) # extender a lista
print(lista_a)