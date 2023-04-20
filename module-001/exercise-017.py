'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt

aSide = float(input('Digite o valor do cateto oposto: '))
bSide = float(input('Digite o valor do cateto adjacente: '))

hypotenuse = sqrt(aSide**2 + bSide**2)

print('O valor da hipotenusa é {:.2f}.'.format(hypotenuse))
