'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep

seconds = 10

print(seconds)

while seconds > 0:
    sleep(1)
    seconds -= 1
    print(seconds)
