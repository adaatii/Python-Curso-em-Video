#Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

n1 = int(input('Digite um numero qualquer: '))
if n1 % 2 == 0:
    print('O numero {} é PAR!'.format(n1))
else:
    print('O numero {} é IMPAR!'.format(n1))
