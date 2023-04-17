'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

phrase = input('Digite uma frase: ').strip().lower()

print('A letra A aparece {} vezes na frase.'.format(phrase.count('a')))
print('A primeira letra A está na posição {}.'.format(phrase.find('a') + 1))
print('A última letra A está na posição {}.'.format(phrase.rfind('a') + 1))
