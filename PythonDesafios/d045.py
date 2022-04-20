#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('OPÇÃO INVÁLIDA')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(1)
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
    if computador == 0:  # Computador jogou Pedra
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')

    elif computador == 1:  # Computador jogou Papel
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')


    elif computador == 2:  # Computadr jogou Tesoura
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')

