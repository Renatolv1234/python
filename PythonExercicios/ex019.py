import random

aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')

lista_alunos = [aluno1,aluno2,aluno3]

escolhido = random.choice(lista_alunos)

print('O aluno escolhido para apagar o quadro é {}'. format(escolhido))