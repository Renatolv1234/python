from math import hypot

co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hipo = hypot(co, ca)
print('A hipotenusa deste triangulo retangulo é {:.2f}'.format(hipo))