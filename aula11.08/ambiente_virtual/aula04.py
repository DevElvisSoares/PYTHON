# Outra forma de interpolar

nome = "Elvis"
salario = 4500.99

print(nome,"ganha um salário de R$ ")
print(f' O salário de {nome} é R$ {salario}')
# forma FORMAT de imprimir
# s - string
# d e i - int
# f - float
# x e X - hexadecimais
print('O salário de %s é R$ %.2f' % (nome,salario))
