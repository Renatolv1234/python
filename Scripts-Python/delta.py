import math

valor_a = float(input('Escreva o valor de a: '))
valor_b = float(input('Escreva o valor de b: '))
valor_c = float(input('Escreva o valor de c: '))

delta = (math.pow(valor_b, 2)) - 4 * valor_a * valor_c

print('O delta desta equiação é {}'.format(delta))