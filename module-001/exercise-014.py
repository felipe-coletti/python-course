'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

c = float(input('Digite uma temperatura em ºC: '))

f = (c * 9 / 5) + 32

print('{:.2f} ºC equivale a {:.2f} ºF.'.format(c, f))
