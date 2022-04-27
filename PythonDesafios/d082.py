# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas.

num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um numero: ')))
    op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
for i in num:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('-='*30)
print(f'A lista caompleta é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
