'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
'''

from math import *

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

h = sqrt(co**2 + ca**2)
