# for trabalha com interaveis
# tem que possuir uma variavel de controle
# metodos: 
# interavel() - tranforma um objeto em iteravel
# next() - função para imprimir os interaveis
# enumerate () é um interador de indices e valores

'''nome = 'Paulo'
for letra in nome:
    print(letra)

letra = iter(nome)
print(next(letra))
print(next(letra))'''

lista_nomes = ['João', 'Pedro', 'Mateus', 'Judas', 'Pedro']

lista_enumerada = enumerate(lista_nomes)
print(lista_nomes)
print(list(lista_enumerada))

for item in lista_enumerada:
    print(item)

for indice_lista, item_lista in enumerate(lista_nomes):
    print(f'{item_lista} é o {indice_lista} da lista')