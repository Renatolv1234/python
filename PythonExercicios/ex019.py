from random import choice

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

lista_alunos = [aluno1,aluno2,aluno3, aluno4]

escolhido = choice(lista_alunos)

print('O aluno escolhido para apagar o quadro é {}'. format(escolhido))