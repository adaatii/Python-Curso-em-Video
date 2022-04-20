#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

produto = float(input('Informe o valor do produto: '))
op = int(input('''Escolha a forma de pagamento:
[1] À vista dinheiro/cheque: 10% de desconto.
[2] À vista no cartão: 5% de desconto.
[3] Em 2x no cartão: preço formal.
[4] 3x ou mais no cartão com 20% de juros.
Sua opção: '''))
if op == 1:
    valorFinal = produto - (produto * 10) / 100
    print('O valor a ser pago será: R${:.2f}'.format(valorFinal))
elif op == 2:
    valorFinal = produto - (produto * 5) / 100
    print('O valor a ser pago será: R${:.2f}'.format(valorFinal))
elif op == 3:
    valorParcela = produto / 2
    print('O valor a ser pago será: 2 parcelas de R${:.2f} = R${:.2f}'.format(valorParcela, produto))
elif op == 4:
    npar = int(input('Informe a quantidade de parcelas: '))
    valorFinal = produto + (produto * 20)/100
    valorParcela = valorFinal / npar
    print('O valor a ser pago será: {} parcelas de R${:.2f} = R${:.2f}'.format(npar, valorParcela, valorFinal))
else:
    print('Opção INVÁLIDA')

