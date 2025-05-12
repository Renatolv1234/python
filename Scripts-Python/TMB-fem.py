nome = input('Qual seu nome?')
idade = input('Quantos anos você tem?')
peso = input('Quanto você pesa?')
altura = input('Qual sua altura?')
tmb = 655 + (9.6 * int(peso)) + (1.8 * int(altura)) - (4.7 * int(idade))

print(nome, 'sua TMB é:', tmb)