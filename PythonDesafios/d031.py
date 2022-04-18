#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
# até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distancia da viagem em km: '))
if distancia > 200:
    valor = distancia * 0.45
    print('O valor a ser pago é de {:.2f} a R$0.45 o km'.format(valor))
else:
    valor = distancia * 0.50
    print('O valor a ser pago é de {:.2f} a R$0.50 o km'.format(valor))
