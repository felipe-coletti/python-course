'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

x = input('Digite algo: ')

print('O tipo primitivo é: {}'.format(type(x)))
print('É composto apenas por espaços? {}'.format(x.isspace()))
print('É composto apenas por números? {}'.format(x.isnumeric()))
print('É composto apenas por letras? {}'.format(x.isalpha()))
print('É composto apenas por números e letras? {}'.format(x.isalnum()))
print('É composto apenas por letras maiúsculas? {}'.format(x.isupper()))
print('É composto apenas por letras minúsculas? {}'.format(x.islower()))
print('Está capitalizado? {}'.format(x.istitle()))
