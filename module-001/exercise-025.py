'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
'''

name = input('Digite um nome completo: ')

print('O nome tem Silva? {}'.format('silva' in name.lower()))
