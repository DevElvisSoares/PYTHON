# uma lista é representadas por []
# len - metodo que retona a quantiddade de itens de uma lista 
# todo metodo por obrigação retorna uma valor
# Lista tem seu proprio CRUD
# Metodos: append, insert, del, remove, pop e len
lista = []
print (lista, type (lista))
print (len(lista))

lista = ['front'] # essa forma sobreescreva a lista anterior
print (lista, type (lista))
print (len(lista))
lista = ['back'] # o valor 'back' sobreescreveu o valor de 'front'
print (lista, type (lista))
print (len(lista))

lista.append('front') # coloca valores no final da lista
print(lista, type (lista))
#          0       1      2   3    4
# reverso -5      -4     -3  -2   -1
lista = ['back', 'tarde', 21, True, 8.8]
print(f' A quantidade de alunos na turna é: {lista [2]}')
lista[2] = 22
print(lista)
lista[1] = ['Neyva', 'Alice', 'Geisa', 'Lara'] # lista dentro da lista
print(lista)

print(lista[-2])
del lista [-2] # deleta pelo indice
print(lista[-2])

lista.remove('back') # remove um item especifico
print(lista)
# lista.pop() remove o ultimo item da lista
# valor_do_pop = lista.pop()
# lista.insert(0, Amontada) = adiciona um item em qualquer lugar

# CRUD - Create, Read, Update, Delete
#        Criar,  Ler,  Atualizar, Deletar  