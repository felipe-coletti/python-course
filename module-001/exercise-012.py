'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

p = float(input('Digite o preço do produto: R$ '))

n = p - (5 / 100 * p)

print('O preço do produto, com um desconto de 5%, vai de R$ {:.2f} para R$ {:.2f}.'.format(p, n))
