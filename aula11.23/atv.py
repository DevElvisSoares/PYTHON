#
#
#
'''texto = input("Digite um texto:")
print(texto)
print(len(texto))

nome = input('Digite um nome: ')
print(nome[0:4])
for i in range(4):
    print(nome[i])

texto1 = input("Digite um nome: ")
texto2 = input("Digite uma frase: ")
if texto1 == texto2:
    print("As palavras são iguais")
else:
    print("As frases são diferentes")

nome1 = input("Digite um nome: ")
vogal = 'a'
vogais2 = 'e'
vogais3 = 'i'
vogais4 = 'o'
vogais5 = 'u'
print(nome1.count(vogal)+ nome1.count(vogais2)+ nome1.count(vogais3) + nome1.count(vogais4)+nome1.count(vogais5))

nome_usuario = input('Digite nome: ')
nome_1 = nome_usuario.replace('a', '')
nome_2 = nome_1.replace('e','')
nome_3 = nome_2.replace('i','')
nome_4 = nome_3.replace('o', '')
nome_5 = nome_4.replace('u','')
print(nome_5)

palavra = input('Digite uma palavra: ')
print(palavra[::-1])'''


nome = input("Digite um nome: ").lower()
vogais = "aeiou"
numero_vogais =  sum(1 for i in nome if i in vogais)
print(numero_vogais)



