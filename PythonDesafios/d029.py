#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada
# Km acima do limite.

velo = float(input('Qual a velocidade do carro? '))
if velo > 80:
    print('Multado! voce excedeu o limite de 80km/h')
    multa = (velo-80)*7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
