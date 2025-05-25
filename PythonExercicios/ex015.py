dia = int(input('Quantos dias você rodou? '))
km = float(input('Quantos KMs você rodou? '))
aluguel = (dia * 60) + (km * 0.15)
print('Você irá pogar R${:.2f} de aluguel!'.format(aluguel))