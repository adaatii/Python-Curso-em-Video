#Crie um programa que leia quanto dinheiro
#uma pessoa tem na carteira e mostre quantos
#dolares ela pode comprar
#Considere US$ 1,00 = R$3,27

n = float(input('Quantos reais você tem na carteira ? '))
print('Seus {} reais equivalem a {} dolares'.format(n, n/3.27))
