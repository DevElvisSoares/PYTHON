# condições ternaria acontece em formato de linha

salario = float(input('Informe o valor do salario: '))

if salario >= 250.00:
    print('IR será cobrado')
else:
    print('IR não será cobrado')

variavel_controle = 'IR será cobrado' if salario  >= 2500.00 else 'IR não será comparado' 
print(variavel_controle)
# variavel_controle 


# Faça uma função que peça um numero e faça o reverso do numero inteiro informado. exemplo: 173 -> 371

def reverso_do_numero (numero):
    reverso = (numero[::-1])
    return int(reverso)

numero = input('Digite um numero: ')
print(f'O reverso do {numero} é {reverso_do_numero(numero)}')



def numero_reverso2 (numero2):
    reverso2 = 0
    while numero > 0:
        #pegar o ultimo valor do numero
        ultimo_valor = numero % 10

        # add ultimo valor
        reverso2 = (reverso2 * 10) + ultimo_valor

        # tira ultimo valor
        numero = numero // 10

        #return reverso
        return reverso2



