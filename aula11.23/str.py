# count - funçao é contar quantas vezes um determinado caractere aparece em uma string.
# upper e lower - Dois metodos que deixam a string toda em maiscula ou em minuscula respectivamente.
# find - busca por uma expreção dentro da frase. 
# replace - é utilizado para realizar alterações dentro das strings
# capitalize - torna a primelra letra em Maiusculo
# split - transforma strings em lista.
frase = "A banana é amarela e o abacate é verde.".lower()
letra = "a"
print(f'A letra {letra} aparece {frase.count(letra)} vezes na frase "{frase}"')
achei = frase.find('soares') # imprimi o indice em que a expresão inicia
if achei >= 0:
    print(f'A expresão foi encontrada no indice {achei}')
else:
    print(f'A expressão não foi encontrada na frase')

saida = input('Digite "s" para sair: ').upper()
if saida == 's':
    print(saida)


print(frase.capitalize())

print(frase.split())




nova_frase = frase.replace("banana", "maracuja") # 
print(frase)
print(nova_frase)