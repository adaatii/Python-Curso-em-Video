# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

listagem = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in listagem:
        listagem.append(n)
    else:
        print('Valor duplicado! Não pode ser adicionado...')
    op = str(input('Desaja continuar? [S/N]'))
    if op in 'Nn':
        break
print('-='*30)
listagem.sort()
print(f'Voce digitou os valors: {listagem}!')

