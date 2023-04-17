'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''

name = input('Digite o nome de uma cidade: ')

firstName = name.split()[0]

print('O nome da cidade começa com Santo? {}'.format(firstName.lower() == 'santo'))
