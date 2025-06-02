import math

fahr = float(input('Digite um valor em grau °C: '))

cel = (fahr - 32) * 5/9

print('{}°F equivalem a {:.2f}°C'.format(fahr,cel))