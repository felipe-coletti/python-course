'''
Crie um programa que leia um número real qualquer e mostra na tela a sua porção inteira.
'''

import math

n = float(input('Digite um número: '))

print('A parte inteira de {} é {}.'.format(n, math.trunc(n)))
