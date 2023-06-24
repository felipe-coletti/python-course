'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

birthYear = int(input('Digite o ano de nascimento: '))

yearsOld = 2023 - birthYear
    
if yearsOld > 18:
    lagTime = yearsOld - 18
    
    if lagTime == 1:
        print('O alistamento foi a {} ano.'.format(lagTime))
    else:
        print('O alistamento foi a {} anos.'.format(lagTime))
elif yearsOld == 18:
    print('O alistamento é nesse ano.')
elif yearsOld < 18 and yearsOld >= 0:
    timeLeft = 18 - yearsOld
    
    if timeLeft == 1:
        print('Falta {} ano até o alistamento.'.format(timeLeft))
    else:
        print('Faltam {} anos até o alistamento.'.format(timeLeft))
else:
    print('Ano de nascimento inválido.')
