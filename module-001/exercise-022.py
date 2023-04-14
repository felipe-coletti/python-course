'''
Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.
'''

name = input('Digite o seu nome completo: ')

firstName = name.split()[0]

print('Seu nome em letras maiúsculas é {}.'.format(name.upper()))
print('Seu nome em letras minúsculas é {}.'.format(name.lower()))
print('Seu nome tem {} letras.'.format(len(name.replace(' ', ''))))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(firstName, len(firstName)))
