#Faça um programa que leia um numero Inteiro
#qualquer e mostre sua tabuada

n = int(input('Informe um numero inteiro: '))

print('A tabuada do {} é:'.format(n))

i = 1
while i <= 10:
    print('{} x {} = {}'.format(n, i, n*i))
    i = i + 1

