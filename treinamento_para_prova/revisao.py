'''resposta = []
for i in range(10):
        nome = input('verdadeiro ou falso: ')
resposta = ...
print(resposta)



# variavel é um espaço na memoria de um computador que recebe um valor

# nome, atribuição de valor e o valor
variavel = 1 # o valor pode ser alterado
print(variavel)

variavel = 'ABCDEFGHIJK'
print(variavel)

# Regra do fatiamentov [inicio, fim, step]

print(variavel[0:9:], variavel[9:12])

frase = 'A casa é azul como o céu'
print(frase[9:24])


# utilizando o fatiamento e repetição imprima uma lista de "a" ate "e" removendo uma letra de cada vez.
lista = ['a', 'b','c','d', 'e' ]

for i in range(6):
    print(lista[:5-i])
    
    

# Estrutura condicionais
variavel = 20
if variavel < 20:
    print('Menor que 20')
elif variavel == 20:
    print('Igual a 20')
          
elif variavel > 20 and variavel <50:
    print('valor mais que 20 e menor que 50')
else:
    print('Qualquer outra coisa')

# estruturas de repetição
# FOR e WHILE
for i in range(10): # também trabalha com (inicio, fim, step)
    print(i)'''

contador = 5
while contador > 0:
    print(contador)
    contador -=1

# Join - unir strings
lista = ['João', 'Paulo', 'II']
nome = '-'.join(lista)
print(nome)