# Fatiamento de strings
# Obs: toda string por padrão é uma lista que não saiu do "armário"
# Ordem de tratamento
# 0123456...
# -654321...

nome = "elvis soares"
print(nome[10]) # posição da letra "e"
print(nome[-2]) # posição da letra "e"
lista_nome = ("e", "l", "v","i","s" )
print(lista_nome[3])

# [i:f:p] = i - INICIO, f - FIM, P - PARSE 

nome = "Antonio Carlos da Silva"
print(nome[8:14]) 
print(nome[-5:])
print(nome[0::2])
print(nome[1::2])