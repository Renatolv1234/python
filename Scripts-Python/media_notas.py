nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))

media = (nota1 + nota2) /2

if media < 5:
    print('Você está reprovado!!')
elif media >= 5 and media <= 6:
    print('Você está de recuperação!!')
else:
    print('Você está aprovado!!')
