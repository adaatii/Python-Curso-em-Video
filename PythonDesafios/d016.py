#Crie um programa que leia um número Real
# qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

num = float(input('Digite um numero Real: '))
print("A porção inteira de {} é {}".format(num, math.floor(num)))

