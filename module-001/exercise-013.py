'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

s = float(input('Digite o salário de um funcionário: R$ '))

n = s + (15 / 100 * s)

print('O salário do funcionário, com um aumento de 15%, vai de R$ {:.2f} para R$ {:.2f}.'.format(p, n))
