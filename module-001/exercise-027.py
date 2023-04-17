'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

name = input('Digite um nome completo: ')

names = name.split()

firstName = names[0]
lastName = names[len(names) - 1]

print('Seu primeiro nome é {}.'.format(firstName))
print('Seu último nome é {}.'.format(lastName))
