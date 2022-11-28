'''
Escreva um programa que leia uma temperatura em graus Celsius e converta para graus Fahrenheit.
'''

c = float(input('Digite uma temperatura em ºC: '))

f = (c * 9 / 5) + 32
k = c + 273.15

print('{:.2f} ºC equivale a {:.2f} ºF e {:.2f} ºK.'.format(c, f, k))
