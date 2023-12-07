# CRUD - Created, Readed, Update e Deled


dic = {'nome':'Paulo'} # Created/criar
dic2 = dict(idade=23) # Created

dic['nome'] # Readed/ler
variavel = dic2.get('idade') # Readed

dic.update(sobrenome = 'Junior') # Updated/atualizar
dic.update({'idade':23}) # Update dicionario
tupla = ('peso', 72.12),
lista = ['data','13/04/1995'], ['numeros', [1, 2, 3, 4, 5, 6, 7, 8, 9 ]]
dic.update(tupla) # Update tupla
dic.update(lista) # Update lista


print(dic)
print(dic2)

dic2.clear() # Deled