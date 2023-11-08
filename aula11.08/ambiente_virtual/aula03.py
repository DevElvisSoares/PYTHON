# Operadores IN E NOT IN

nome = "Elvis"
print('vi' in nome)

print('='*20)

seu_nome = input('Informe seu nome: ')
buscar = input('Informe o valor a ser encontrado: ')

if (buscar in seu_nome):
    print(f'{buscar} está contido em {seu_nome}')
else:
    print(f'{buscar} não está contido em {seu_nome}')


nao_nome = "Joãozinho"
print("au" not in nao_nome)