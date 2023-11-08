nome = "Elvis"
altura = 1.73
peso = 64
imc = peso / (altura * altura) # os tres pontos indica que o python está esperando um valor a ser definido.

# A resposta dessa questão deve ser:
# Fulano tem ALT de x, pesa PES X e

print(nome,"tem", altura,"de altura")
print("pesa", peso,"quilos e seu IMC é: ")
print(imc)

# Codigo mais limpo
print(f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é: ')
print(f'{imc:.2f}') 