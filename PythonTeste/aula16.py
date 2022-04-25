lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são Imutáveis
print(lanche)
print(lanche[-2])
print(lanche[1:3])  # vai da psosição 1 a 2 ignorando o ultimo elemento 3
print(lanche[2:])
print(lanche[:2])  # ignora o ultimo elemento
print(lanche[-3:])
for comida in lanche:
    print('E vou comer {}'.format(comida))
for cont in range(0, len(lanche)):
    print('E vou comer {} na posição {}'.format(lanche[cont], cont))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(5, 1))

pessoa = ('Lucas', 29, 'M', 76.5)
print(pessoa)
