preco = float(input('Qual o preço do produto? R$'))
desconto = preco - (preco*0.05)
print('Com desconto de 5% você irá deixar de pagar R${:.2f} e irá pagar R${:.2f}!'.format(preco,desconto))
