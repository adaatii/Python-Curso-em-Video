#Faça um programa que leia a largura e a altura de uma parede
#em metros, calcule a sua área e a quantidade de tinta necessaria
#para pinta-la, sabendo que cada litro de tinta, pinta uma area
#de 2m²

alt = float(input('Digite a altura: '))
lar = float(input('Digite a largura: '))
print('A quantida de tinta para pintar {}m² é de {} litros'.format(alt*lar, (alt*lar)/2))
