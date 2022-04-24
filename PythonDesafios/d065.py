op = 'S'
soma = qtd = media = maior = menor =0
while op == 'S':
    num = int(input('Digite um numero: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    op = str(input('Deseja continuar: [S/N]')).strip().upper()
media = soma / qtd
print('Voce digitou {} numeros e a média foi {}'.format(qtd, media))
print('O menor valor {} e o maior valor foi {}'.format(menor, maior))
