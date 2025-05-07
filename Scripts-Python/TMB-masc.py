nome = input('Qual seu nome?')
idade = input('Qual sua idade?')
peso = input('Quanto você pesa(em kg)?')
altura = input('Qual sua altura(em cm)?')
tmb = 66 + (13.7 * int(peso)) + (5 * int(altura)) - (6.8 * int(idade))

print(nome, 'sua TMB é', tmb)
