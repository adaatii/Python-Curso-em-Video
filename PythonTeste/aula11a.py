a = 3
b = 5
print('Os valores são \33[32m{}\33[m e \33[31m{}\33[m!!!'.format(a, b))


cores = {'limpa': '\33[m',
         'azul': '\33[34m',
         'amarelo': '\33[33m',
         'pretoebranco': '\33[7;30m'}
nome = 'Lucas'
print('Ola! Muito prazer em te conhecer {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))


