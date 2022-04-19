# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.

print('-='*20)
print('SIMULADOR DE EMPRESTIMO')
print('-='*20)
valorcasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salario: '))
qtdanos = int(input('Informe quantos anos de financiamento: '))

meses = qtdanos*12
valorparcela = valorcasa / meses
porcentagemsalario = (salario * 30)/100

if valorparcela <= porcentagemsalario:
    print('Emprestimo aprovado. O valor da parcela será de R${:.2f} a ser pago nos proximos {} meses.'.format(valorparcela, meses))
else:
    print('Emprestimo NEGADO! O valor da parcela excede 30% do salario.')