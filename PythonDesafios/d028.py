#Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo
# computador. O programa deverá escrever na tela se
# o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)#faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar ...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei ? '))#jogador informa o numero
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens voce conseguiu me vencer')
else:
    print('GANHEI. Eu pensei no numero {} e não no numero {}'.format(computador, jogador))
