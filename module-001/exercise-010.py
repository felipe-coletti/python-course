'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''

r = float(input('Digite um valor em reais: '))

d = r / 3.27

print('R$ {:.2f} equivale a USD$ {:.2f}.'.format(r, d))
