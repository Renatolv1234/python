nome = input('Qual seu nome?')
peso = int(input('Qual seu peso?'))
altura = int(input('Qual sua altura?'))
imc = peso/altura**2

print('{} seu IMC é {}'.format(nome, imc))
