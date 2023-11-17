# Questão 1.
lista = [1, 2, 3, 4, 5]
print(lista)
del lista [2]
print(lista)

# Questão 2.
lista2 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 16.0]
print(lista2 [1:10:2])
print(lista2[0:10:2])

# Questão 3.
aluno_nota1 = float(input('Digiete a primeira nota: '))
aluno_nota2 = float(input('Digiete a segunda nota: '))
aluno_nota3 = float(input('Digiete a terceira nota: '))
media1 = (aluno_nota1 + aluno_nota2 + aluno_nota3) / 3

aluno2_nota1 = float(input('Digiete a primeira nota: '))
aluno2_nota2 = float(input('Digiete a segunda nota: '))
aluno2_nota3 = float(input('Digiete terceira nota: '))
media2 = (aluno2_nota1 + aluno2_nota2 + aluno2_nota3) / 3

aluno3_nota1 = float(input('Digiete a primeira nota: '))
aluno3_nota2 = float(input('Digiete a segunda nota: '))
aluno3_nota3 = float(input('Digiete a terceira nota: '))
media3 = (aluno3_nota1 + aluno3_nota2 + aluno3_nota3) / 3

lista_de_medias = [media1, media2, media3]
print(lista_de_medias)

# Questão 4.
lista_consoante = []
letra1 = input('Digite a primeira letra: ')
if letra1 != 'a' and letra1 != 'e' and letra1 and letra1 != 'i' and 'o' and letra1 != 'u':
    print('É consoante')
    lista_consoante = [letra1]
letra2 = input('Digite a segunda letra: ')
if letra2 != 'a' and letra2 != 'e' and letra2 and letra2 != 'i' and 'o' and letra2 != 'u':
    print('É consoante')
    lista_consoante.append(letra2)
letra3 = input('Digite a terceira letra: ')
if letra3 != 'a' and letra3 != 'e' and letra3 and letra3 != 'i' and letra3 != 'o' and letra3 != 'u':
    print('É consoante')
    lista_consoante.append(letra3)
letra4 = input('Digite a quarta letra: ')
if letra4 != 'a' and letra4 != 'e' and letra4 and letra4 != 'i' and letra4 != 'o' and letra4 != 'u':
    print('É consoante')
    lista_consoante.append(letra4)
letra5 = input('Digite a quinta letra: ')
if letra5 != 'a' and letra5 != 'e' and letra5 and letra5 != 'i' and letra5 != 'o' and letra5 != 'u':
    lista_consoante.append(letra5)
    print('É consoante')
print(lista_consoante)


# Questão 5.
lista_inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_pares = (lista_inteiros[1:20:2])
print(lista_pares)
lista_impares = (lista_inteiros[0:20:2])
print(lista_impares)