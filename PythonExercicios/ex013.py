sal = float(input('Qual o salário do funcionário? R$'))
aumento = sal + (sal*15/100)
print('O salário que antes erá R${:.2f}, com 15% de aumento, passa a ser R${:.2f}'.format(sal, aumento))
