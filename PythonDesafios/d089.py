# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('Opção inválida. Tente novamente.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    resp = str(input('Deseja ver as notas de um dos alunos? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    elif resp != 'S' and resp != 'N':
        print('Opção inválida. Tente novamente.')
    else:
        print('-' * 35)
        opc = int(input('Mostrar notas de qual aluno? :'))
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    # Resolução do professor:
    '''print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    elif opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')'''
print('VOLTE SEMPRE')
