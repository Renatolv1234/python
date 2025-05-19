nome = input('Nome do aluno: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('A média do aluno {} é de {:.1f}'.format(nome, media))