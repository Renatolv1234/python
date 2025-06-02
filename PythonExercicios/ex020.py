from random import shuffle
'''O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um pseudocodigo que leia o nome dos alunos e mostre a ordem sorteada'''

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

lista_alunos = [aluno1,aluno2,aluno3]

'''Não necessita escrever random.shuffle'''

shuffle(lista_alunos)

print('A ordem de apresentação é \n{}'.format(lista_alunos))