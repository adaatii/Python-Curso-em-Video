# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = totMil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    '''else:
        if preco < menor:
            menor = preco
            barato = produto'''
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print('O total da campra foi R${:.2f}'.format(total))
print('Temos {} produto custando mais de R$1000'.format(totMil))
print('O produto mais barato foi {} que custa R${}.'.format(barato, menor))
