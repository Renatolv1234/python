nome = input('Qual seu nome?')
idade = int(input('Quantos anos você tem?'))
peso = int(input('Quanto você pesa?'))
altura = int(input('Qual sua altura?'))
tmb = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

print('{} sua TMB é: {}'.format(nome, tmb))