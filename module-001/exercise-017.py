'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

from math import *

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

h = sqrt(co**2 + ca**2)

print('O valor da hipotenusa é {:.2f}.'.format(h))
