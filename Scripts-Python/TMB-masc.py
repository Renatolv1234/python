nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))
peso = int(input('Quanto você pesa(em kg)?'))
altura = int(input('Qual sua altura(em cm)?'))
tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)

print('{} sua TMB é: {}'.format(nome, tmb))
