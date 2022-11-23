b = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

a = b * h

l = a / 2

print('A área de uma parede de {:.2f}x{:.2f} é de {:.2f} m² e, para pinta-la, será necessário {:.2f} L de tinta.'.format(b, h, a, l))
