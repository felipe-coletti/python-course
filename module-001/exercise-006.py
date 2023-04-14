'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

number = float(input('Digite um número: '))

double = number * 2
triple = number * 3
squareRoot = number**(1/2)

print('O dobro de {} é {}.'.format(number, double))
print('O triplo de {} é {}.'.format(number, triple))
print('A raiz quadrada de {} é {}.'.format(number, squareRoot))
