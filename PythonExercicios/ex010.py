real = float(input('Quanto você tem na carteira? R$'))
dol = real / 5.66
print('Com R${} você irá conseguir comprar US${:.2f}!'.format(real,dol))