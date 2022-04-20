#Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+r2:
    print('Os segmentos informados PODEM FORMAR UM TRIÂNGULO ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 and r2 !=r3 and r1 != r3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos informados NÃO PODEM FORMAR UM TRIÂNGULO!')