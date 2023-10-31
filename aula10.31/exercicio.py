
distancia = float(input("Qual a distancia em Km ? "))
litros = float(input("Qual o valor do consumo de combustivel em litros? "))
consumo_por_litro = distancia / litros
if consumo_por_litro < 8:
    print("Venda o carro")
elif consumo_por_litro >= 8 and consumo_por_litro <= 14:
    print("Econômico")
else:
    print("Super ecônomico")