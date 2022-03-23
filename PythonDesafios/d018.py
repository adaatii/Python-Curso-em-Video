#Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.
import math

ang = float(input('Informe um angulo qualquer: '))
print('O seno, o cosseno e a tangente de {} são, respectivamente, {:.1f} | {:.1f} | {:.1f}'
      .format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))
