# imprima na tela os pares dentro de uma lista chamada pares_ok
# remova da lista os multiplos de 4
meus_numeros = [0, 1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares_ok = (meus_numeros[2::2])
print(pares_ok)
del meus_numeros [0::4]
print(meus_numeros)


 
# imprima na tela os multiplos de 3 em uma lista chamada multiplos_ok
# remova de meus_numeros os multiplos de 5 
meus_numeros = [0, 1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
multiplos_ok = (meus_numeros[0::3])
print(multiplos_ok)
del meus_numeros [0::5]
print(meus_numeros)



# imprima na tela uma lista só com os nomes que não começam com 'R'
# remova os nomes dos indices impares
meus_nomes = ['Ricardo', 'Roberto', 'Soares', 'Rivaldo', 'Richard', 'Andre']
print([meus_nomes[2] , meus_nomes[5]])
del meus_nomes [1]
del meus_nomes[3]
del meus_nomes [3]
print(meus_nomes)
