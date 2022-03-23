#Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa
import math

catop = float(input('Informe o cateto oposto: '))
catad = float(input('Informe o cateto adjacente: '))

hip = math.sqrt((catop**2)+(catad**2))

print('A o comprimento da hipotenuza é: {}'.format(hip))

