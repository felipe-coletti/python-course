'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior;
- O segundo valor é maior;
- Não existe valor maior, os dois são iguais.
'''

firstNumber = int(input('Digite o primeiro número: '))
secondNumber = int(input('Digite o segundo número: '))

if firstNumber > secondNumber:
    print('O primeiro número é maior.')
elif secondNumber > firstNumber:
    print('O segundo número é maior.')
else:
    print('Os dois números são iguais.')
