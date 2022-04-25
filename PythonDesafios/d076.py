# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 10,
            'Compasso', 7.95,
            'Mochila', 150.45,
            'Canetas', 22.30,
            'Livro', 34.50)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')
print('-'*40)

