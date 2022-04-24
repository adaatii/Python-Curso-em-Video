# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele
# conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()
    print('Voce jogou {} e o computador {}. Total de {} '.format(jogador, computador, total))
    print('DEU PAR ' if total % 2 == 0 else 'DEU ÍMPAR ', end='')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU')
            v += 1
        else:
            print('Voce PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU')
            v += 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente... ')
print('GAMEOVER! Voce venceu {} vezes.'.format(v))