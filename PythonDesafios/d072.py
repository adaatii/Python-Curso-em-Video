cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO',
        'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
        'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE',
        'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
        'DEZENOVE', 'VINTE')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
       break
    print('Tente novamente \n', end='')
print('Você digitou o numero {}.'.format(cont[num]))
