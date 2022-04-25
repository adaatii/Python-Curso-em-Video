# Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um  numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valors: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu {num.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado.')
print('Os numeros pares foram: ')
for i in num:
    if i % 2 ==0:
        print(i, end=' ')
    else:
        print('Não foram digitados numeros pares')
        break
