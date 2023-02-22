'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import *

a = float(input('Digite o valor de um ângulo: '))

s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('O seno de {:.2f} é {:.2f}.'.format(a, s))
print('O cosseno de {:.2f} é {:.2f}.'.format(a, c))
print('A tangente de {:.2f} é {:.2f}.'.format(a, t))
