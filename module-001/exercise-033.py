'''
Faça um programa que leia três números e mostre qual é o menor e qual é o maior.
'''

firstNumber = float(input('Digite o primeiro número: '))
secondNumber = float(input('Digite o segundo número: '))
thirdNumber = float(input('Digite o terceiro número: '))

smallerNumber = higherNumber = firstNumber

if secondNumber < smallerNumber:
    smallerNumber = secondNumber
if thirdNumber < smallerNumber:
    smallerNumber = thirdNumber

if secondNumber > higherNumber:
    higherNumber = secondNumber
if thirdNumber > higherNumber:
    higherNumber = thirdNumber

print('O menor número é {} e o maior número é {}.'.format(smallerNumber, higherNumber))
