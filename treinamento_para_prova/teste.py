lista = [0,1,2,3,4,5,6,7,8,9,]
print(len(lista))

lista.append(10)

print(lista)

del lista[3]

print (lista)

lista.remove(10)
print(lista)

lista.append(10)
lista.insert(3,3)
print(lista)



frase = "A maça esta podre".lower()
letra = 'a'
nova_frase = frase.replace('maça', 'abacaxi')
print(nova_frase)
print(frase.count(letra))


nome00 = input("Digite um nome: ")
vogais_nome = sum(1 for i in nome00 if i in "aeiou" )
print(vogais_nome)

contador = 0
nome1 = input('digite um nome: ')
for i in nome1:
    if i in "aeiou":
        contador += 1
print(contador)