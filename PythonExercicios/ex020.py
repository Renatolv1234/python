import random
'''O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um pseudocodigo que leia o nome dos alunos e mostre a ordem sorteada'''

aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('nome do terceiro aluno: ')

lista_alunos = [aluno1,aluno2,aluno3]

primeiro = random.choice(lista_alunos)
segundo = random.choice((lista_alunos))
terceiro = random.choice(lista_alunos)

print('A ordem de apresentação é 1° o {} depois o {} e por ultimo {}'.format(primeiro,segundo,terceiro))