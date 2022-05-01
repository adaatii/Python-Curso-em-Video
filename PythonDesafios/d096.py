# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def lin():
    print('-'*30)


'''def area():
    largura = float(input('Digite a largura do terreno: [M] '))
    comprimento = float(input('Digite o comprimento do terreno: [M] '))
    result = largura * comprimento
    print(f'Com a largura de {largura} e comprimento de {comprimento} ', end=''
          f'a area do terreno é de {result} M²')

lin()
print('     CONTROLE DE TERRENOS       ')
lin()
area()'''

def area(larg, comp):

    result = largura * comprimento
    print(f'Com a largura de {largura} e comprimento de {comprimento} ', end=''
          f'a area do terreno é de {result} m²')



lin()
print('     CONTROLE DE TERRENOS       ')
lin()
largura = float(input('Digite a largura do terreno: (m) '))
comprimento = float(input('Digite o comprimento do terreno: (m) '))
area(largura, comprimento)



