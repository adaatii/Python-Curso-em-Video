# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = date.today().year
nasc = int(input('digite o ano de nascimento: '))
idade = ano - nasc
print('Quem nasceu em {} tem em {} anos em {}.'.format(nasc, ano, idade))
if idade == 18:
    print('Voce deve se alista Imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} ano/s para o alistamento.'.format(saldo))
    alis = ano + saldo
    print('Seu alistamento será em {}'.format(alis))
elif idade > 18:
    saldo = idade - 18
    print('Passou {} ano/s para o alistamento.'.format(saldo))
    alis = ano - saldo
    print('Seu alistamento foi em {}'.format(alis))
