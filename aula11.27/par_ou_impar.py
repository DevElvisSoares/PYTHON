# Para bibliotecas e metodos
# no terminal digita python 
# import random e veja as bibliotecas e metodos.
from random import randint # Para que o random importe somente randint , impot random para importar todos os metodos)

placar_jogador1 = 0
placar_computador = 0

while True:

    jogador1 = input("Escolha par ou impar: ").lower()
    if jogador1 == 'par':
        computador = 'impar'
    else:
        computador = 'par'

    numero1 = int(input("Digite um numero: "))
    numero_do_computador = randint (0,10)

    resultado = numero1 + numero_do_computador


    if resultado %2 == 0:
        if jogador1 == 'par':
            print(f'Jogador1 venceu!!!numero do jogador1 {numero1} numero do computador {numero_do_computador}')
            placar_jogador1 += 1
        else:
            print(f'O computador venceu!!!!{numero1},{numero_do_computador}')
            placar_computador += 1
    else:
        if jogador1 == 'impar':
            print(f'O jogador1 venceu!!!numero do jogador1 {numero1} numero do computador {numero_do_computador}')
            placar_jogador1 += 1
        else:
            print(f'O computador venceu!!!numero do jogador1 {numero1} numero do computador {numero_do_computador}')
            placar_computador += 1
        print(f'O placar está de {placar_jogador1} x {placar_computador}')
