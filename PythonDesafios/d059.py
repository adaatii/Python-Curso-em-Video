#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import  sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('Qual sua opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif op == 2:
        produto = n1 * n2
        print('A multiplicação entre {} * {} = {}'.format(n1, n2, produto))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando ...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa')
