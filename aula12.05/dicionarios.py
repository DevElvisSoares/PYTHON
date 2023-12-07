# Dicionario - é uma coleção de itens que possuem chave e valor
# Dicionarios são mutaveis
# criando e modificando um dicionario
d = {'user':'Marciel', 'password':2324}
print(type(d))
# parametro {} 
# dic = {} ou dic = dict()
# possuem chave(keys) e valores(values)
# metodos : has_key('eggs'), clear(), del d['key'], values(), items(),get(), update()

#copy() fazer copias de dicionarios

pessoa = {'nome': 'paulo', 'sobrenome' : 'Junior'}
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())

k = pessoa.keys() # a variavel vai receber somente o valor das chaves{}
v = pessoa.values() # a variavel vai receber somente o valor de values(valores)

for chave, valor in pessoa.items():
    print(chave,valor)


print(pessoa['sobrenome'])

print('='*140)


d1 = {'valor1': 100,'valor2':200, 'valores3':300}
 
d2 = d1 # o d2 é só um apontamento do d1, não é um dicionario proprio

d2['valor2'] = 2000
print(d1)


outros_valores = {'valore4':500, 'valor5': 600 }
d1.update(outros_valores)
print(d1)
