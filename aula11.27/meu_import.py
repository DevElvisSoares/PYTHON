preco = float(input("Informe o preço do produto: "))

desconto01 = 0.2 # 20%
desconto02 = 0.5 # 50%
desconto03 = 0.8 # 80%
valor = preco * desconto02
print(valor)

if preco < 100:
    valor = preco * desconto01
elif preco >= 100 and preco <=500:
    valor = preco * desconto02
elif preco > 500:
    valor = preco * desconto03
else:
    print("O valor não está na tabela de descontos.")
print(valor)