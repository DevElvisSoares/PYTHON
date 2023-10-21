# Calculo p/ homens: (72.7*h) - 58
# Calculo p/ mulheres: (62.1*h) - 44.7

h = float(input("Digite a sua altura: "))
sexo = input("Informe seu sexo, masculino ou feminino: ")
if sexo == 'masculino' :
    peso_ideal = (72.7 * h) - 58
    print(f'seu peso ideal é {peso_ideal}kg.')

else:
    peso_ideal = (62.1 * h) - 44.7
    print(f'seu peso ideal é {peso_ideal}kg.')