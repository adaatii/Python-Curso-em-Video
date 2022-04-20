#Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido em OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Valor inválido. Tente novamente.')