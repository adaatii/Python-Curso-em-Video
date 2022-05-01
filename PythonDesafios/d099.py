# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*num):
    cont = m = 0
    print('-='*30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(valor, end=' ')
        sleep(0.3)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    print(f'\nO maior valor informado foi {m}.')


maior(9, 8, 6, 15)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
