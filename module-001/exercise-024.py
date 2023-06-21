'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "Santo".
'''

name = input('Digite o nome de uma cidade: ')

nameParts = name.split()

firstNamePart = nameParts[0]

print('O nome da cidade começa com Santo? {}'.format(firstNamePart.lower() == 'santo'))
