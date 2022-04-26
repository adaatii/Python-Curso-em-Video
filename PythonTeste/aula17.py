num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(3)# se o parenteses estiver vazio ele retira o ultimo elemento.
num.remove(2)# elimina apenas o primeiro elemento encontrado
if 5 in num:
    num.remove(5)
else:
    print('Valor 5 não encontrado')
print(num)
print(f'Essa lista tem {len(num)} elementos.')


valores= list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')


