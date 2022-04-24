# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('''Digite o numero da tabuada que quer ver
[Numero NEGATIVO sai do programa]: '''))
    if num < 0:
        break
    else:
        print('-='*30)
        for i in range (1, 11):
            print('{} x {} = {}'.format(num, i, (num*i)))

        print('-=' * 30)
print('Programa de tabuada ENCERRADO.')