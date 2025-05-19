n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1+n2
su = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma vale {}, o produto vale {}, e a divisão vale {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e exponeciação {}'.format(di, e))