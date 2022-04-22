#Refaça o DESAFIO 9, mostrando a tabuada
# de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Digite o numero da tabuada que deseja ver: '))
for i in range(1, 11):
    print('{} X {} = {}'.format(i, num, i*num))