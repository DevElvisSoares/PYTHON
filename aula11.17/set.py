# Set - conjutos
# Set não garante ordem
# Set não possui indice
# Set não aceitam objetos duplicados
# parametros: {} 
#metodos: add, update, clear e discard
# criando um set: set('Paulo') ou {1, 3, 5, 7}

set01 = set('Paulo') # Esse metodo só aceita objetos interaveis
print(set01)

set02 = {'Paulo', 'Junior'} # objetos
print(set02)


lista = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
set03 = set(lista)
print(set03)

for i in set03:
    print(i)

set03.add('Elvis')
print(set03)

set03.add(6)
print(set03)
set03.update('Elvis')
print(set03)
set03.discard('Elvis')
print(set03)
set03.clear() # Esse comando limpa o set ou conjunto
print(set03)

set04 = {1, 2, 3, 4, 5}
set05 = {4, 5, 6, 7, 8}
set06 = set04 | set05 # União de conjuntos
print(set06)
set06 = set04 & set05 # Interseção de conjuntos
print(set06)

set06 = set04 - set05
print(set06)