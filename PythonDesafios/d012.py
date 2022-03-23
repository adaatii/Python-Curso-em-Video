#Faça um algoritimo que leia o preço de um produto
#e mostre seu novo preço, com 5% de desconto.

preco = float(input('Informe o valor do produto: '))
print('O valor {} com 5% de desconto é de: {}'.format(preco, preco - (preco*0.05)))
