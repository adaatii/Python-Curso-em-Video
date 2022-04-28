# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]
num = 0
for i in range(0, 7):
    num = int(input(f'Digite o {i+1}° valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('-='*30)
lista[0].sort()
lista[1].sort()
print(f'A lista de valores pares é: {lista[0]}')
print(f'A lista de valores ímpares é: {lista[1]}')
