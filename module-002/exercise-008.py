'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status: abaixo de 18,5 o status será "Abaixo do peso", de 18,5 a 24,9 o status será "Peso ideal", de 25 a 29,9 o status será "Sobrepeso", de 30 a 39,9 o status será "Obesidade" e a partir de 40 o status será "Obesidade mórbida".
'''

mass = float(input('Digite o peso: '))
height = float(input('Digite a altura: '))

bmi = mass / height**2

print('O IMC é de {:.2f} Kg/m².'.format(bmi))

if bmi > 40:
    print('Status: Obesidade mórbida.')
elif bmi >= 30:
    print('Status: Obesidade.')
elif bmi >= 25:
    print('Status: Sobrepeso.')
elif bmi >= 18.5:
    print('Status: Peso ideal.')
else:
    print('Status: Abaixo do peso.')
