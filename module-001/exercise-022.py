'''
Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.
'''

name = input('Digite um nome completo: ')

firstName = name.split()[0]

print('O nome em letras maiúsculas é {}.'.format(name.upper()))
print('O nome em letras minúsculas é {}.'.format(name.lower()))
print('O nome tem {} letras.'.format(len(name.replace(' ', ''))))
print('O primeiro nome é {} e ele tem {} letras.'.format(firstName, len(firstName)))
