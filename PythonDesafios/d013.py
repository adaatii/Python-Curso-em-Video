#Faça um algoritimo que leia o salário do funcionário
#e mostre seu novo salário com 15% de aumento.

salarioAtual = float(input('Informe o salario do funcionário: '))
salarioNovo = salarioAtual + (salarioAtual*0.15)
print('O salario de {} com aumento de 15% será igual a: {}'.format(salarioAtual, salarioNovo))
