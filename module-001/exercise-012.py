p = float(input('Digite o preço do produto: R$ '))

n = p - (5 / 100 * p)

print('O preço do produto com um desconto de 5% é de R$ {:.2f}.'.format(n))
