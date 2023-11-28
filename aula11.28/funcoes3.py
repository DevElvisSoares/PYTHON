# Faça uma funçãs que informa a quantidade de digito de um numero imteiro

'''def quant_digito (numero):
    resultado = len(numero)
    return (resultado)

numero = input('Digite um numero: ') 
print(quant_digito(numero))'''



# Escreva uma função chamada gorjeta que recebe o valor da conta de um restaurante. Calcule e exibe a gorjeta do garçom, considerando 12% do valor da conta 
def gorjeta (valor):
    valor_garcom = valor * 0.12 
    return valor_garcom
    

valor = float(input('Infome o valor da conta: '))
print(gorjeta(valor))