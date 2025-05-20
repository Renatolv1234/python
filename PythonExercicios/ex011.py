larg = float(input('Qual a largura de sua parede?'))
alt = float(input('Qual a altura da sua parede?'))
area = larg * alt
tinta = area /2
print('Você precisará de {:.1f} litros de tinta para pintar essa parede com uma área de {:.2f}m²!'.format(tinta, area))
