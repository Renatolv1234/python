nome = input('Digite o nome do aluno: ')
n1 = input('Nota da primeira prova: ')
n2 = input('Nota da segunda prova: ')
n3 = input('Nota da terceira prova: ')
media = (int(n1) + int(n2) + int(n3))/3

print('A média do aluno {}'.format(nome),',foi de {}'.format(media))
