#Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for i in range(0, 6):
    num = int(input('Digite o {}° valor: '.format(i+1)))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 1:
    print('Voce me informou {} numero Par e a soma foi {}'.format(cont, soma))
else:
    print('Voce me informou {} numeros Pares e a soma foi {}'.format(cont, soma))
