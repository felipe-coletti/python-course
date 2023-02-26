'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import *

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segunundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

l = [a1, a2, a3, a4]

print('O aluno sorteado foi {}.'.format(shuffle(l)))
