# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-='*15)
print('Lista de Times:')
for t in times:
    print(t)
print('-='*15)
print('Os 5 primeiro são: ')
times_prim = times[:5]
for i in times_prim:
    print(i)
print('-='*15)
print('Os 4 ultimos são: ')
times_ult = times[-4:]
for i in times_ult:
    print(i)
print('-='*15)
print('Times em ordem alfabética: ')
lista_alfa = sorted(times)
for i in lista_alfa:
    print(i)
print('-='*15)
print('O chapecoense está na {}° posição'.format(times.index('Chapecoense')+1))

