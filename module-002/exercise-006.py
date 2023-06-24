'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: quem tiver até 9 anos será mirim, de 10 a 14 anos será infantil, de 15 a 19 anos será júnior, de 20 a 25 anos será sênior e a partir de 25 anos será master.
'''

from datetime import date

birthYear = int(input('Digite o ano de nascimento: '))

currentYear = date.today().year

if birthYear <= currentYear:
    yearsOld = currentYear - birthYear
    
    if yearsOld > 25:
        category = 'Master'
    elif yearsOld >= 20:
        category = 'Sénior'
    elif yearsOld >= 15:
        category = 'Júnior'
    elif yearsOld >= 10:
        category = 'Infantil'
    else:
        category = 'Mirim'
        
    print('A categoria é: {}'.format(category))
else:
    print('Ano de nascimento inválido.')
