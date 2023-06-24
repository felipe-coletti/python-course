'''
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: equilátero (quando todos os lados são iguais), isósceles (quando só dois lados são iguais) ou escaleno (quando todos os lados são diferentes).
'''

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Os segmentos de reta a, b e c podem formar um triângulo equilátero.')
    elif a != b != c != a:
        print('Os segmentos de reta a, b e c podem formar um triângulo escaleno.')
    else:
        print('Os segmentos de reta a, b e c podem formar um triângulo isósceles.')
else:
    print('Os segmentos de reta a, b e c não podem formar um triângulo.')
