# Tuplas são imutaveis
# parametro: ()

tupla = (1, 2, 3, 4, 5)
print(tupla[1])
tupla[1] = 6 # Perceba que dá erro, pois  a tupla é  imutavel

# se você não definir o parametro da lista ou tupla com [] ou (), o python tranforma para tupla, por conta da imutabilidade.