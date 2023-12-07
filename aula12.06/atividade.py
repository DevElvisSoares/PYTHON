# 1.0 Crie um lista de alunos com nome e nota final de cada aluno. Coloque em um dicionario, depois imprima.
'''dic = {}
lista = [['Elvis',10] ,['Francisco',10], ['Eduardo', 10]]
dic.update(lista)
print(dic)

# 2.0 Ainda sobre a questão 1.0 iserir mais 4 alunos e notas  no seu dicionario.

#lista_nova = [['Mikael', 10],['Arthur', 10],['Kaynan', 10],['Jeferson',10]]
#dic.update(lista_nova) 
# OU
dic.update({'Paulo':10,'Felipe':10,'Junior':10,'Alice':10})
print(dic)

#  3.0 faça um código que pede a marca e o modelo ao cliente
lista_marca_model = []

marca = input('Informe a marca do carro: ')
modelo = input('Infome o modelo do carro: ')

lista_marca_model.append(marca)
lista_marca_model.append(modelo)

dic_carros = {}
dic_carros.update([lista_marca_model])

print(lista_marca_model)
print(dic_carros)

dic_carros['Fiat'] = 'Uno'
print(dic_carros)

# 4.0  Crie um cadastro de clientes recebendo nome, idade, data de aniversario e endereço completo. Adicione todas as informações em um dicionario. Imorima.
dic_cadastro = {}
#for i in range(5):
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
data_aniversario = input('Informe sua data de aniversario: ')
endereco = input('Informe seu endereço: ')

lista_inforçoes = []
lista_inforçoes.append(nome)
lista_inforçoes.append(idade)
lista_inforçoes.append(data_aniversario)
lista_inforçoes.append(endereco)

dic_cadastro.update([lista_inforçoes])
print(dic_cadastro)'''


# 5.0 Crie um sistema de login e senha. Crie um dicionario contendo os acessos dos colaboradores com nome de usuario e senha, em seguida peça as informações e valide o longin do usuario.
sistama_dados = {'eduardo':123, 'elvis': 321, 'kaynan':1010}
dic_dados = {}
login = input('Informe o seu login :')
senha = int(input('Informe sua senha: '))


dic_dados[login]=senha


if login in sistama_dados and  sistama_dados[login] == senha:
      
        print('Acesso liberado')
else:
        print('login ou senha incorreto')


