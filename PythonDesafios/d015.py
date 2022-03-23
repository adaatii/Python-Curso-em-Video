#Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a
# pagar, sabendo que o carro custa R$60 por dia e R$0,15
# por Km rodado.

dias = int(input('Informe a quantidade de dias alugados:'))
km = float(input('Informe a quantidade km percorridos: '))
print('O carro foi alugado por {} dias com {}Km percorridos,'
      ' gerando um total a pagar de: {}'.format(dias, km, (dias*60)+(km*0.15)))
