nome = str(input('Qual é seu nome? ').strip().capitalize())
#Estrutura condicional aninhada.
if nome == 'Lucas':
    print('Que nome bonito')
elif nome == 'Mabi':
    print('Seu nome é bem diferente')
else:
    print('Que nome normal.')
print('Tenha um bom dia, {}!'.format(nome))
