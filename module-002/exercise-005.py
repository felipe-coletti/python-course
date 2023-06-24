'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: alunos com a média abaixo de 5 são reprovados, alunos com a média entre 5 e 6,9 ficam de recuperação e alunos com a média 7 ou superior são aprovados.
'''

firstGrade = float(input('Digite a primeira nota: '))
secondGrade = float(input('Digite a segunda nota: '))

average = (firstGrade + secondGrade) / 2

print('A média é {:.2f}.'.format(average))

if average >= 7:
    print('O aluno foi aprovado.')
elif average >= 5:
    print('O aluno terá que fazer uma prova de recuperação.')
else:
    print('O aluno foi reprovado.')

