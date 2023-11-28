# funções são blocos de codigos que são executados somente quando são chamados 
# parametro : def
# as funções devem ter prioridades no código

def media (nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

nota1 = int(input('Digita a primeira nota: '))
nota2 = int(input('Digite a sgunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
print(media( nota1 ,  nota2, nota3))


def calcule_horas_extras (quantidas_horas, valor_hora):
    horas = float(quantidas_horas)
    taxa = float(valor_hora)

    if horas >= 40:
        valor_receber = (horas - 40) * taxa
    return valor_receber

quantidade_horas = float(input('Informe o total de horas trabalhadas: ')) 
valor_da_hora = float(input('Informe o valor da taxa do colaborador: '))

print (calcule_horas_extras(quantidade_horas, valor_da_hora))

# Faça um programa com uma função que necessite de um argumento. A função retorna o valor de caracter 'P', se seu argumento for positivo, 'N' se argumento for negativo ou zero.

def valor_argumento (argumento01):
    argumento = int(argumento01)
    if argumento01 > 0:
        valor_argumento = " P"
    else: 
        valor_argumento = "N"
    return valor_argumento

argumento01 = int(input('Digite um valor: '))
print(valor_argumento(argumento01))











