# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

listagem = []
while True:
    listagem.append(int(input('Digite um valor: ')))
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op in 'N':
        break
print(f'A quantidade de numeros digitados foi {len(listagem)}')
listagem.sort(reverse=True)
print(f'A lista em ordem decrescente é: {listagem}')
if 5 in listagem:
    print('O numero 5 foi digitado e está na lista')
else:
    print('O numero 5 não foi digitado e não está na lista ')
