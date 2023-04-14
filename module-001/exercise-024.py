'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''

cityName = input('Digite o nome da cidade onde você nasceu: ')

cityFirstName = cityName.split()[0]

print('O nome da cidade começa com Santo? {}'.format(cityFirstName.lower() == 'santo'))
