n = input('Digite algo: ')
print(' É Numérico ? {} \n É Alfabético ? {} \n Começa com letra Maiuscula ? '
      '{} \n Começa com letra Minuscula? {}\n'.format(n.isnumeric(), n.isalpha(), n.isupper(), n.islower()))
