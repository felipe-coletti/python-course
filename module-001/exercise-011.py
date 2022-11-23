b = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

a = b * h

l = a / 2

print('A área de uma parede com as dimensões {}x{} é de {} m².'.format(b, h, a))
print('Para pinta-la, será necessário {} L de tinta.'.format(l))
