#Escreva um programa que leia um malor em metros
#e o exiba convertido em centimetros e milimetros

n = float(input('Digite um valor em metros: '))
cent = n * 100
mil = n * 1000
print('O valor em centimetros é: {} cm'.format(cent))
print('O valor em milimetros é: {} mm'.format(mil))
